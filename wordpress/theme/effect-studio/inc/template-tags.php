<?php
/**
 * توابع کمکی قالب.
 *
 * @package Effect_Studio
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * منوی پیش‌فرض اصلی (وقتی منویی در پیشخوان تنظیم نشده باشد).
 */
function effect_studio_primary_menu_fallback() {
	$items = array(
		__( 'استودیو اثر', 'effect-studio' ) => home_url( '/' ),
		__( 'درباره ما', 'effect-studio' )  => home_url( '/about-us/' ),
		__( 'خدمات اثر', 'effect-studio' )  => home_url( '/#services' ),
		__( 'بلاگ', 'effect-studio' )        => home_url( '/blog/' ),
		__( 'فروشگاه', 'effect-studio' )     => home_url( '/shop/' ),
		__( 'ارتباط با ما', 'effect-studio' ) => home_url( '/#contact' ),
	);

	echo '<ul class="menu">';
	foreach ( $items as $label => $url ) {
		printf(
			'<li class="menu-item"><a href="%1$s">%2$s</a></li>',
			esc_url( $url ),
			esc_html( $label )
		);
	}
	echo '</ul>';
}

/**
 * آدرس آکادمی.
 */
function effect_studio_academy_url() {
	return apply_filters( 'effect_studio_academy_url', home_url( '/academy/' ) );
}

/**
 * شماره تلفن برند.
 */
function effect_studio_phone() {
	return apply_filters( 'effect_studio_phone', '۰۹۱۵ ۳۸۹ ۲۰۸۸' );
}

/**
 * ایمیل برند.
 */
function effect_studio_email() {
	return apply_filters( 'effect_studio_email', 'hello@effect.studio' );
}

/**
 * آیکون‌های شبکه‌های اجتماعی.
 */
function effect_studio_social_icons() {
	$networks = array(
		'instagram' => array( __( 'اینستاگرام', 'effect-studio' ), 'https://instagram.com/' ),
		'telegram'  => array( __( 'تلگرام', 'effect-studio' ), 'https://t.me/' ),
		'youtube'   => array( __( 'یوتیوب', 'effect-studio' ), 'https://youtube.com/' ),
		'linkedin'  => array( __( 'لینکدین', 'effect-studio' ), 'https://linkedin.com/' ),
		'facebook'  => array( __( 'فیسبوک', 'effect-studio' ), 'https://facebook.com/' ),
	);

	$paths = array(
		'instagram' => '<path d="M12 2.2c3.2 0 3.6 0 4.9.1 3.3.1 4.8 1.7 4.9 4.9.1 1.3.1 1.6.1 4.8 0 3.2 0 3.6-.1 4.8-.1 3.2-1.7 4.8-4.9 4.9-1.3.1-1.6.1-4.9.1-3.2 0-3.6 0-4.8-.1-3.3-.1-4.8-1.7-4.9-4.9-.1-1.3-.1-1.6-.1-4.8 0-3.2 0-3.6.1-4.8.1-3.2 1.7-4.8 4.9-4.9 1.2-.1 1.6-.1 4.8-.1Zm0 1.8c-3.1 0-3.4 0-4.6.1-2.4.1-3.4 1-3.5 3.5-.1 1.2-.1 1.5-.1 4.6s0 3.4.1 4.6c.1 2.4 1 3.4 3.5 3.5 1.2.1 1.5.1 4.6.1s3.4 0 4.6-.1c2.4-.1 3.4-1 3.5-3.5.1-1.2.1-1.5.1-4.6s0-3.4-.1-4.6c-.1-2.4-1-3.4-3.5-3.5-1.2-.1-1.5-.1-4.6-.1Zm0 3.1a4.9 4.9 0 1 1 0 9.8 4.9 4.9 0 0 1 0-9.8Zm0 1.8a3.1 3.1 0 1 0 0 6.2 3.1 3.1 0 0 0 0-6.2Zm5.1-3.1a1.2 1.2 0 1 1 0 2.4 1.2 1.2 0 0 1 0-2.4Z"/>',
		'telegram'  => '<path d="M21.9 4.4 18.7 19c-.2 1-.8 1.3-1.7.8l-4.7-3.5-2.3 2.2c-.3.3-.5.5-1 .5l.4-4.8L18.2 6c.4-.3-.1-.5-.6-.2L7.3 12.3l-4.6-1.4c-1-.3-1-1 .2-1.5l17.8-6.9c.8-.3 1.6.2 1.2 1.9Z"/>',
		'youtube'   => '<path d="M21.6 7.2a2.5 2.5 0 0 0-1.8-1.8C18.2 5 12 5 12 5s-6.2 0-7.8.4A2.5 2.5 0 0 0 2.4 7.2 26 26 0 0 0 2 12a26 26 0 0 0 .4 4.8 2.5 2.5 0 0 0 1.8 1.8C5.8 19 12 19 12 19s6.2 0 7.8-.4a2.5 2.5 0 0 0 1.8-1.8A26 26 0 0 0 22 12a26 26 0 0 0-.4-4.8ZM10 15.2V8.8L15.2 12 10 15.2Z"/>',
		'linkedin'  => '<path d="M4.98 3.5A2.49 2.49 0 1 1 5 8.48a2.49 2.49 0 0 1-.02-4.98ZM3 9h4v12H3V9Zm7 0h3.8v1.7h.05c.53-1 1.83-2.06 3.77-2.06C21.6 8.64 23 10.9 23 14v7h-4v-6.2c0-1.5 0-3.4-2.06-3.4s-2.38 1.6-2.38 3.3V21H10V9Z"/>',
		'facebook'  => '<path d="M14 8.5V6.8c0-.8.2-1.2 1.3-1.2H17V2h-3.1C10.6 2 9.5 4.3 9.5 6.4v2.1H7v3.6h2.5V21H14v-8.9h3l.5-3.6h-3.5Z"/>',
	);

	foreach ( $networks as $key => $data ) {
		list( $label, $url ) = $data;
		$url = apply_filters( "effect_studio_social_{$key}_url", $url );
		printf(
			'<a href="%1$s" aria-label="%2$s" target="_blank" rel="noopener noreferrer"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">%3$s</svg></a>',
			esc_url( $url ),
			esc_attr( $label ),
			$paths[ $key ] // مسیر SVG ثابت و امن است.
		);
	}
}
