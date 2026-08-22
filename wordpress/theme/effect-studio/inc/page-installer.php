<?php
/**
 * نصب خودکار صفحات هنگام فعال‌سازی قالب.
 *
 * با فعال شدن قالب، ۹ صفحه سایت (خانه، درباره ما، آکادمی، دوره، بلاگ،
 * دسته‌بندی، نوشته، فروشگاه، محصول) ساخته می‌شوند و محتوای المنتور آن‌ها
 * (از فایل‌های JSON در inc/pages/) به‌صورت خودکار بارگذاری می‌شود.
 * سپس صفحه نخست، صفحه نوشته‌ها و منوی اصلی تنظیم می‌شوند.
 *
 * @package Effect_Studio
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * نسخه المنتور که قالب‌ها با آن تولید شده‌اند.
 * اگر المنتور فعال باشد، نسخه واقعی جایگزین می‌شود.
 */
if ( ! defined( 'EFFECT_STUDIO_ELEMENTOR_VERSION' ) ) {
	define( 'EFFECT_STUDIO_ELEMENTOR_VERSION', '3.20.0' );
}

/**
 * اجرای نصب صفحات (یک‌بار).
 */
function effect_studio_install_pages() {
	if ( get_option( 'effect_studio_pages_installed' ) ) {
		return;
	}

	$dir = get_template_directory() . '/inc/pages';
	if ( ! is_dir( $dir ) ) {
		return;
	}

	$ids        = array();
	$front_page = '';
	$posts_page = '';
	$menu_items = array();

	foreach ( glob( $dir . '/*.json' ) as $file ) {
		$raw = file_get_contents( $file );
		$tpl = json_decode( $raw, true );

		if ( ! is_array( $tpl ) || empty( $tpl['slug'] ) ) {
			continue;
		}

		$slug  = sanitize_title( $tpl['slug'] );
		$title = isset( $tpl['title'] ) ? $tpl['title'] : $slug;

		// اگر صفحه از قبل وجود داشت، فقط شناسه آن را نگه می‌داریم.
		$existing = get_page_by_path( $slug, OBJECT, 'page' );
		if ( $existing ) {
			$ids[ $slug ] = $existing->ID;
		} else {
			$post_id = wp_insert_post(
				array(
					'post_title'   => $title,
					'post_name'    => $slug,
					'post_type'    => 'page',
					'post_status'  => 'publish',
					'post_content' => '',
				)
			);

			if ( $post_id && ! is_wp_error( $post_id ) ) {
				$ids[ $slug ] = $post_id;

				// ذخیره محتوای المنتور (فقط بدنه؛ هدر/فوتر توسط قالب رندر می‌شود).
				update_post_meta( $post_id, '_elementor_edit_mode', 'builder' );
				update_post_meta( $post_id, '_elementor_template_type', 'wp-page' );
				update_post_meta( $post_id, '_elementor_version', EFFECT_STUDIO_ELEMENTOR_VERSION );
				update_post_meta( $post_id, '_elementor_page_settings', '[]' );
				// حذف CSS کهنه تا المنتور آن را از نو تولید کند.
				delete_post_meta( $post_id, '_elementor_css' );
				if ( ! empty( $tpl['content'] ) ) {
					update_post_meta( $post_id, '_elementor_data', wp_slash( wp_json_encode( $tpl['content'] ) ) );
				}
			}
		}

		// ثبت پرچم‌های ویژه.
		if ( ! empty( $tpl['front_page'] ) ) {
			$front_page = $slug;
		}
		if ( ! empty( $tpl['posts_page'] ) ) {
			$posts_page = $slug;
		}
		if ( ! empty( $tpl['menu'] ) && isset( $ids[ $slug ] ) ) {
			$menu_items[] = array(
				'label'   => $tpl['menu'],
				'page_id' => $ids[ $slug ],
			);
		}
	}

	// تنظیم صفحه نخست و صفحه نوشته‌ها.
	if ( $front_page && isset( $ids[ $front_page ] ) ) {
		update_option( 'show_on_front', 'page' );
		update_option( 'page_on_front', $ids[ $front_page ] );
	}
	if ( $posts_page && isset( $ids[ $posts_page ] ) ) {
		update_option( 'page_for_posts', $ids[ $posts_page ] );
	}

	// ساختار پیوند یکتا.
	update_option( 'permalink_structure', '/%postname%/' );

	// ساخت منوی اصلی و اتصال به موقعیت «منوی اصلی».
	if ( ! empty( $menu_items ) ) {
		effect_studio_create_primary_menu( $menu_items );
	}

	update_option( 'effect_studio_pages_installed', 1 );
	flush_rewrite_rules();

	// پاک‌سازی کش CSS المنتور تا صفحات از نو ساخته شوند.
	effect_studio_clear_elementor_cache();
}
add_action( 'after_switch_theme', 'effect_studio_install_pages' );

/**
 * پاک‌سازی کش CSS المنتور (برای اینکه صفحات تازه‌ساخته شده به‌درستی رندر شوند).
 */
function effect_studio_clear_elementor_cache() {
	// اگر المنتور فعال نیست، کاری نمی‌کنیم (بعداً هنگام فعال‌شدن خودش CSS می‌سازد).
	if ( ! class_exists( '\Elementor\Plugin' ) ) {
		return;
	}

	// حذف فایل‌های CSS مربوط به صفحات قالب (تا از نو تولید شوند).
	$pages = get_pages( array( 'number' => -1 ) );
	foreach ( $pages as $page ) {
		if ( get_post_meta( $page->ID, '_elementor_edit_mode', true ) === 'builder' ) {
			$css = \Elementor\Core\Files\CSS\Post::create( $page->ID );
			if ( method_exists( $css, 'delete' ) ) {
				$css->delete();
			}
		}
	}

	// پاک‌سازی کش عمومی فایل‌های المنتور.
	if ( method_exists( \Elementor\Plugin::$instance, 'files_manager' ) && is_callable( array( \Elementor\Plugin::$instance->files_manager, 'clear_cache' ) ) ) {
		\Elementor\Plugin::$instance->files_manager->clear_cache();
	}
}

/**
 * ساخت منوی اصلی از آیتم‌های مشخص‌شده.
 *
 * @param array $items آرایه‌ای از آیتم‌ها با کلیدهای label و page_id.
 */
function effect_studio_create_primary_menu( $items ) {
	$menu_name = __( 'منوی اصلی', 'effect-studio' );

	$menu = wp_get_nav_menu_object( $menu_name );
	if ( ! $menu ) {
		$menu_id = wp_create_nav_menu( $menu_name );
	} else {
		$menu_id = $menu->term_id;
	}

	// اتصال به موقعیت «منوی اصلی».
	$locations            = get_theme_mod( 'nav_menu_locations', array() );
	$locations['primary'] = $menu_id;
	set_theme_mod( 'nav_menu_locations', $locations );

	foreach ( $items as $item ) {
		if ( empty( $item['page_id'] ) ) {
			continue;
		}
		wp_update_nav_menu_item(
			$menu_id,
			0,
			array(
				'menu-item-title'     => $item['label'],
				'menu-item-object'    => 'page',
				'menu-item-object-id' => $item['page_id'],
				'menu-item-type'      => 'post_type',
				'menu-item-status'    => 'publish',
			)
		);
	}
}

/**
 * اعلان مدیریتی بعد از نصب صفحات.
 */
function effect_studio_pages_installed_notice() {
	if ( ! get_option( 'effect_studio_pages_installed' ) ) {
		return;
	}
	if ( get_option( 'effect_studio_pages_notice_dismissed' ) ) {
		return;
	}
	?>
	<div class="notice notice-success is-dismissible">
		<p>
			<?php esc_html_e( 'قالب استودیو اثر فعال شد و ۹ صفحه سایت به‌صورت خودکار ساخته شدند. برای نمایش کامل محتوا، افزونه المنتور را فعال کنید.', 'effect-studio' ); ?>
		</p>
	</div>
	<?php
}
add_action( 'admin_notices', 'effect_studio_pages_installed_notice' );
