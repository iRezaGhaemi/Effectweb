<?php
/**
 * Effect Studio theme functions and definitions.
 *
 * @package Effect_Studio
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit; // دسترسی مستقیم ممنوع.
}

define( 'EFFECT_STUDIO_VERSION', '1.0.0' );

/**
 * راه‌اندازی قالب
 */
function effect_studio_setup() {
	// پشتیبانی از عنوان خودکار در <head>.
	add_theme_support( 'title-tag' );

	// تصویر شاخص برای نوشته‌ها و برگه‌ها.
	add_theme_support( 'post-thumbnails' );

	// لوگوی سفارشی.
	add_theme_support(
		'custom-logo',
		array(
			'height'      => 43,
			'width'       => 130,
			'flex-height' => true,
			'flex-width'  => true,
		)
	);

	// خروجی HTML5.
	add_theme_support(
		'html5',
		array( 'search-form', 'comment-form', 'comment-list', 'gallery', 'caption', 'style', 'script' )
	);

	// فید خودکار.
	add_theme_support( 'automatic-feed-links' );

	// ویرایشگر بلوکی با عرض کامل.
	add_theme_support( 'align-wide' );

	// پشتیبانی از رنگ پس‌زمینه سفارشی (فقط هنگام استفاده از ویرایشگر بلوک).
	add_theme_support(
		'editor-color-palette',
		array(
			array( 'name' => __( 'Royal', 'effect-studio' ), 'slug' => 'royal', 'color' => '#4a00a5' ),
			array( 'name' => __( 'Why', 'effect-studio' ), 'slug' => 'why', 'color' => '#2d0065' ),
			array( 'name' => __( 'Amber', 'effect-studio' ), 'slug' => 'amber', 'color' => '#ffaa00' ),
			array( 'name' => __( 'Ink', 'effect-studio' ), 'slug' => 'ink', 'color' => '#16161d' ),
			array( 'name' => __( 'Body', 'effect-studio' ), 'slug' => 'body', 'color' => '#3d4350' ),
		)
	);

	// ثبت منوهای ناوبری.
	register_nav_menus(
		array(
			'primary' => __( 'منوی اصلی', 'effect-studio' ),
			'footer'  => __( 'منوی فوتر', 'effect-studio' ),
		)
	);

	// ترجمه قالب.
	load_theme_textdomain( 'effect-studio', get_template_directory() . '/languages' );
}
add_action( 'after_setup_theme', 'effect_studio_setup' );

/**
 * عرض محتوا (بدون نوار کناری).
 */
function effect_studio_content_width() {
	$GLOBALS['content_width'] = apply_filters( 'effect_studio_content_width', 1280 );
}
add_action( 'after_setup_theme', 'effect_studio_content_width', 0 );

/**
 * بارگذاری استایل‌ها و اسکریپت‌ها.
 */
function effect_studio_scripts() {
	$dir = get_template_directory_uri();

	// استایل اصلی قالب.
	wp_enqueue_style( 'effect-studio-style', get_stylesheet_uri(), array(), EFFECT_STUDIO_VERSION );

	// فونت وزیرمتن (با جایگزین محلی در صورت وجود).
	$font_url = apply_filters(
		'effect_studio_font_url',
		'https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800;900&display=swap'
	);
	wp_enqueue_style( 'effect-studio-font', $font_url, array(), null );

	// اسکریپت اصلی (منوی موبایل و ...).
	wp_enqueue_script( 'effect-studio-main', $dir . '/assets/js/main.js', array(), EFFECT_STUDIO_VERSION, true );

	if ( is_singular() && comments_open() && get_option( 'thread_comments' ) ) {
		wp_enqueue_script( 'comment-reply' );
	}
}
add_action( 'wp_enqueue_scripts', 'effect_studio_scripts' );

/**
 * کلاس‌های <body>.
 */
function effect_studio_body_classes( $classes ) {
	// کلاس برای صفحات راست‌چین (همیشه در این قالب).
	$classes[] = 'rtl';

	if ( is_front_page() ) {
		$classes[] = 'effect-front-page';
	}
	if ( function_exists( 'elementor_theme_do_location' ) ) {
		$classes[] = 'elementor-active';
	}
	return $classes;
}
add_filter( 'body_class', 'effect_studio_body_classes' );

/**
 * فیلتر عنوان صفحه.
 */
function effect_studio_document_title_parts( $title ) {
	return $title;
}
add_filter( 'document_title_parts', 'effect_studio_document_title_parts' );

/**
 * نمایش لوگو یا نام سایت.
 */
function effect_studio_the_logo() {
	if ( has_custom_logo() ) {
		the_custom_logo();
		return;
	}
	$name = get_bloginfo( 'name' );
	echo '<a class="brand" href="' . esc_url( home_url( '/' ) ) . '" rel="home">';
	echo '<span class="brand-fallback">' . esc_html( $name ) . '</span>';
	echo '</a>';
}

/**
 * ثبت ناحیه‌های ویجت (اختیاری).
 */
function effect_studio_widgets_init() {
	register_sidebar(
		array(
			'name'          => __( 'ناحیه فوتر', 'effect-studio' ),
			'id'            => 'footer-widgets',
			'description'   => __( 'ویجت‌های ستون‌های فوتر.', 'effect-studio' ),
			'before_widget' => '<div id="%1$s" class="footer-col %2$s">',
			'after_widget'  => '</div>',
			'before_title'  => '<h4>',
			'after_title'   => '</h4>',
		)
	);
}
add_action( 'widgets_init', 'effect_studio_widgets_init' );

/**
 * بارگذاری تنظیمات سفارشی (Customizer).
 */
require get_template_directory() . '/inc/customizer.php';

/**
 * قالب‌های بخش‌ها.
 */
require get_template_directory() . '/inc/template-tags.php';
