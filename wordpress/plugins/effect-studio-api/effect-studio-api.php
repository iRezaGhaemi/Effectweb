<?php
/**
 * Plugin Name: Effect Studio REST API
 * Description: اندپوینت‌های REST اختصاصی برای فرانت‌اند headless استودیو اثر. هر بخش سایت (خانه، درباره ما، آکادمی، دوره، بلاگ، فروشگاه) یک اندپوینت اختصاصی دارد.
 * Version: 1.0.0
 * Author: Effect Studio
 * Text Domain: effect-studio-api
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * کلاس اصلی API.
 */
final class Effect_Studio_REST_API {

	const NAMESPACE = 'effect/v1';

	public function __construct() {
		add_action( 'rest_api_init', array( $this, 'register_routes' ) );
	}

	/**
	 * ثبت همه مسیرها.
	 */
	public function register_routes() {
		// اطلاعات سراسری (برند، ناوبری، تماس).
		register_rest_route(
			self::NAMESPACE,
			'/global',
			array(
				'methods'             => WP_REST_Server::READABLE,
				'callback'            => array( $this, 'get_global' ),
				'permission_callback' => '__return_true',
			)
		);

		// صفحه اصلی.
		register_rest_route(
			self::NAMESPACE,
			'/home',
			array(
				'methods'             => WP_REST_Server::READABLE,
				'callback'            => array( $this, 'get_home' ),
				'permission_callback' => '__return_true',
			)
		);

		// بخش‌های صفحه‌ای (about / academy / course) به‌صورت داینامیک.
		register_rest_route(
			self::NAMESPACE,
			'/section/(?P<slug>[a-zA-Z0-9-]+)',
			array(
				'methods'             => WP_REST_Server::READABLE,
				'callback'            => array( $this, 'get_section' ),
				'permission_callback' => '__return_true',
				'args'                => array(
					'slug' => array(
						'validate_callback' => function ( $param ) {
							return is_string( $param );
						},
					),
				),
			)
		);

		// فهرست نوشته‌ها (بلاگ).
		register_rest_route(
			self::NAMESPACE,
			'/posts',
			array(
				'methods'             => WP_REST_Server::READABLE,
				'callback'            => array( $this, 'get_posts' ),
				'permission_callback' => '__return_true',
			)
		);

		// یک نوشته.
		register_rest_route(
			self::NAMESPACE,
			'/posts/(?P<slug>[a-zA-Z0-9-]+)',
			array(
				'methods'             => WP_REST_Server::READABLE,
				'callback'            => array( $this, 'get_post' ),
				'permission_callback' => '__return_true',
			)
		);

		// فهرست محصولات (ووکامرس).
		register_rest_route(
			self::NAMESPACE,
			'/products',
			array(
				'methods'             => WP_REST_Server::READABLE,
				'callback'            => array( $this, 'get_products' ),
				'permission_callback' => '__return_true',
			)
		);
	}

	/**
	 * اطلاعات سراسری: برند، ناوبری، تماس.
	 */
	public function get_global() {
		return array(
			'name'    => get_bloginfo( 'name' ),
			'desc'    => get_bloginfo( 'description' ),
			'url'     => home_url(),
			'phone'   => get_theme_mod( 'effect_studio_phone', '۰۹۱۵ ۳۸۹ ۲۰۸۸' ),
			'email'   => get_theme_mod( 'effect_studio_email', 'hello@effect.studio' ),
			'nav'     => $this->get_nav(),
			'social'  => $this->get_social(),
		);
	}

	/**
	 * داده‌های صفحه اصلی (ترکیب ACF + آخرین نوشته‌ها).
	 */
	public function get_home() {
		$front = (int) get_option( 'page_on_front' );

		return array(
			'hero'     => array(
				'title'    => $this->acf( $front, 'hero_title', 'هم مسیر تا تغییر' ),
				'subtitle' => $this->acf( $front, 'hero_subtitle', '' ),
			),
			'services' => $this->acf_repeater( $front, 'services', 'name' ),
			'stats'    => $this->acf( $front, 'stats', '' ),
			'why'      => $this->acf( $front, 'why', '' ),
			'latest'   => $this->get_posts(),
		);
	}

	/**
	 * داده‌های یک بخش (about / academy / course) بر اساس اسلاگ برگه.
	 */
	public function get_section( $request ) {
		$slug = sanitize_title( $request['slug'] );

		$page = get_page_by_path( $slug, OBJECT, 'page' );
		if ( ! $page ) {
			return new WP_Error( 'not_found', __( 'بخش یافت نشد.', 'effect-studio-api' ), array( 'status' => 404 ) );
		}

		$id = $page->ID;

		$data = array(
			'slug'  => $slug,
			'title' => get_the_title( $id ),
			'hero'  => $this->acf( $id, 'hero_text', '' ),
			'body'  => $this->acf( $id, 'body', '' ),
		);

		// فیلدهای اختصاصی هر بخش.
		if ( 'academy' === $slug ) {
			$courses        = $this->acf_repeater( $id, 'courses', array( 'title', 'desc' ) );
			$data['courses'] = $courses;
		}
		if ( 'course' === $slug ) {
			$data['curriculum'] = $this->acf( $id, 'curriculum', '' );
		}

		return $data;
	}

	/**
	 * فهرست نوشته‌ها.
	 */
	public function get_posts() {
		$query = new WP_Query(
			array(
				'post_type'      => 'post',
				'posts_per_page' => 20,
				'post_status'    => 'publish',
			)
		);

		$items = array();
		foreach ( $query->posts as $p ) {
			$items[] = $this->format_post( $p );
		}

		return $items;
	}

	/**
	 * یک نوشته بر اساس اسلاگ.
	 */
	public function get_post( $request ) {
		$slug = sanitize_title( $request['slug'] );
		$p    = get_page_by_path( $slug, OBJECT, 'post' );

		if ( ! $p ) {
			return new WP_Error( 'not_found', __( 'نوشته یافت نشد.', 'effect-studio-api' ), array( 'status' => 404 ) );
		}

		return $this->format_post( $p );
	}

	/**
	 * فهرست محصولات ووکامرس (در صورت فعال بودن).
	 */
	public function get_products() {
		if ( ! class_exists( 'WooCommerce' ) ) {
			return array();
		}

		$query = new WP_Query(
			array(
				'post_type'      => 'product',
				'posts_per_page' => 20,
				'post_status'    => 'publish',
			)
		);

		$items = array();
		foreach ( $query->posts as $p ) {
			$product = wc_get_product( $p->ID );
			if ( ! $product ) {
				continue;
			}
			$items[] = array(
				'slug'  => $product->get_slug(),
				'title' => $product->get_name(),
				'price' => $product->get_price_html(),
				'desc'  => wp_strip_all_tags( $product->get_short_description() ),
				'image' => get_the_post_thumbnail_url( $p->ID, 'large' ),
			);
		}

		return $items;
	}

	// ---------------------------------------------------------------------
	// توابع کمکی
	// ---------------------------------------------------------------------

	/**
	 * خواندن یک فیلد ACF با مقدار پیش‌فرض.
	 */
	private function acf( $post_id, $name, $default = '' ) {
		if ( function_exists( 'get_field' ) ) {
			$val = get_field( $name, $post_id );
			if ( $val ) {
				return $val;
			}
		}
		return $default;
	}

	/**
	 * خواندن repeater از ACF. اگر $fields آرایه باشد، اشیای کلیددار برمی‌گرداند؛
	 * اگر رشته باشد، لیست ساده.
	 */
	private function acf_repeater( $post_id, $name, $fields ) {
		if ( ! function_exists( 'have_rows' ) ) {
			return array();
		}

		$out = array();
		if ( have_rows( $name, $post_id ) ) {
			while ( have_rows( $name, $post_id ) ) {
				the_row();
				if ( is_array( $fields ) ) {
					$item = array();
					foreach ( $fields as $f ) {
						$item[ $f ] = get_sub_field( $f );
					}
					$out[] = $item;
				} else {
					$out[] = get_sub_field( $fields );
				}
			}
		}
		return $out;
	}

	/**
	 * منوی ناوبری.
	 */
	private function get_nav() {
		$items  = array();
		$menus  = get_nav_menu_locations();
		if ( ! empty( $menus['primary'] ) ) {
			$nav = wp_get_nav_menu_items( $menus['primary'] );
			if ( $nav ) {
				foreach ( $nav as $item ) {
					$items[] = array(
						'label' => $item->title,
						'href'  => $item->url,
					);
				}
			}
		}
		return $items;
	}

	/**
	 * شبکه‌های اجتماعی.
	 */
	private function get_social() {
		return array(
			'instagram' => apply_filters( 'effect_studio_social_instagram_url', 'https://instagram.com/' ),
			'telegram'  => apply_filters( 'effect_studio_social_telegram_url', 'https://t.me/' ),
			'youtube'   => apply_filters( 'effect_studio_social_youtube_url', 'https://youtube.com/' ),
			'linkedin'  => apply_filters( 'effect_studio_social_linkedin_url', 'https://linkedin.com/' ),
		);
	}

	/**
	 * فرمت‌دهی یک نوشته.
	 */
	private function format_post( $p ) {
		return array(
			'slug'    => $p->post_name,
			'title'   => get_the_title( $p ),
			'excerpt' => wp_strip_all_tags( get_the_excerpt( $p ) ),
			'body'    => apply_filters( 'the_content', $p->post_content ),
			'date'    => get_the_date( '', $p ),
			'image'   => get_the_post_thumbnail_url( $p, 'large' ),
		);
	}
}

new Effect_Studio_REST_API();
