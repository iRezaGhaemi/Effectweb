<?php
/**
 * هماهنگی قالب با ووکامرس.
 *
 * این فایل فقط زمانی که افزونه ووکامرس فعال باشد بارگذاری می‌شود
 * (با بررسی class_exists در is_woocommerce_active).
 *
 * @package Effect_Studio
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * آیا ووکامرس فعال است؟
 */
function effect_studio_is_woocommerce_active() {
	return class_exists( 'WooCommerce' );
}

/**
 * اعمال تنظیمات ووکامرس.
 */
function effect_studio_woocommerce_setup() {
	if ( ! effect_studio_is_woocommerce_active() ) {
		return;
	}

	// تعداد ستون‌های فروشگاه.
	add_filter(
		'loop_shop_columns',
		function () {
			return 3;
		}
	);

	// تعداد محصولات در هر صفحه فروشگاه.
	add_filter(
		'loop_shop_per_page',
		function () {
			return 12;
		}
	);

	// حذف استایل پیش‌فرض ووکامرس (استایل برند جایگزین می‌شود).
	add_filter( 'woocommerce_enqueue_styles', '__return_empty_array' );
}
add_action( 'after_setup_theme', 'effect_studio_woocommerce_setup' );

/**
 * افزودن استایل اختصاصی ووکامرس برند.
 */
function effect_studio_woocommerce_scripts() {
	if ( ! effect_studio_is_woocommerce_active() ) {
		return;
	}

	wp_enqueue_style(
		'effect-studio-woocommerce',
		get_template_directory_uri() . '/assets/css/woocommerce.css',
		array( 'effect-studio-style' ),
		EFFECT_STUDIO_VERSION
	);
}
add_action( 'wp_enqueue_scripts', 'effect_studio_woocommerce_scripts' );

/**
 * بسته‌بندی محتوای ووکامرس با ظرف قالب.
 */
function effect_studio_woocommerce_before_main_content() {
	echo '<div class="container entry-content"><div class="wc-effect-wrap">';
}
add_action( 'woocommerce_before_main_content', 'effect_studio_woocommerce_before_main_content', 5 );

/**
 * بستن ظرف محتوای ووکامرس.
 */
function effect_studio_woocommerce_after_main_content() {
	echo '</div></div>';
}
add_action( 'woocommerce_after_main_content', 'effect_studio_woocommerce_after_main_content', 5 );

/**
 * تنظیم صفحه فروشگاه ووکامرس (یک‌بار، بعد از فعال‌سازی قالب).
 */
function effect_studio_woocommerce_assign_shop_page() {
	if ( ! effect_studio_is_woocommerce_active() ) {
		return;
	}
	if ( get_option( 'effect_studio_wc_shop_page_set' ) ) {
		return;
	}

	// اگر صفحه‌ای با اسلاگ shop وجود دارد، آن را به‌عنوان صفحه فروشگاه تنظیم می‌کنیم.
	$shop = get_page_by_path( 'shop', OBJECT, 'page' );
	if ( $shop ) {
		update_option( 'woocommerce_shop_page_id', $shop->ID );
	}

	update_option( 'effect_studio_wc_shop_page_set', 1 );
}
add_action( 'after_switch_theme', 'effect_studio_woocommerce_assign_shop_page', 20 );
