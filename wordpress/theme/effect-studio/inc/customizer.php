<?php
/**
 * تنظیمات سفارشی (Customizer) برای رنگ‌ها و اطلاعات برند.
 *
 * @package Effect_Studio
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * ثبت تنظیمات سفارشی.
 */
function effect_studio_customize_register( $wp_customize ) {

	// بخش تنظیمات برند.
	$wp_customize->add_section(
		'effect_studio_brand',
		array(
			'title'    => __( 'تنظیمات برند اثر', 'effect-studio' ),
			'priority' => 30,
		)
	);

	// شماره تلفن.
	$wp_customize->add_setting(
		'effect_studio_phone',
		array(
			'default'           => '۰۹۱۵ ۳۸۹ ۲۰۸۸',
			'sanitize_callback' => 'sanitize_text_field',
		)
	);
	$wp_customize->add_control(
		'effect_studio_phone',
		array(
			'label'   => __( 'شماره تلفن', 'effect-studio' ),
			'section' => 'effect_studio_brand',
			'type'    => 'text',
		)
	);

	// ایمیل.
	$wp_customize->add_setting(
		'effect_studio_email',
		array(
			'default'           => 'hello@effect.studio',
			'sanitize_callback' => 'sanitize_email',
		)
	);
	$wp_customize->add_control(
		'effect_studio_email',
		array(
			'label'   => __( 'ایمیل', 'effect-studio' ),
			'section' => 'effect_studio_brand',
			'type'    => 'email',
		)
	);

	// رنگ اصلی برند.
	$wp_customize->add_setting(
		'effect_studio_royal',
		array(
			'default'           => '#4a00a5',
			'sanitize_callback' => 'sanitize_hex_color',
		)
	);
	$wp_customize->add_control(
		new WP_Customize_Color_Control(
			$wp_customize,
			'effect_studio_royal',
			array(
				'label'   => __( 'رنگ اصلی برند', 'effect-studio' ),
				'section' => 'effect_studio_brand',
			)
		)
	);

	// رنگ تاکیدی (کهربایی).
	$wp_customize->add_setting(
		'effect_studio_amber',
		array(
			'default'           => '#ffaa00',
			'sanitize_callback' => 'sanitize_hex_color',
		)
	);
	$wp_customize->add_control(
		new WP_Customize_Color_Control(
			$wp_customize,
			'effect_studio_amber',
			array(
				'label'   => __( 'رنگ تاکیدی (CTA)', 'effect-studio' ),
				'section' => 'effect_studio_brand',
			)
		)
	);
}
add_action( 'customize_register', 'effect_studio_customize_register' );

/**
 * اعمال رنگ‌های سفارشی به CSS.
 */
function effect_studio_customize_css() {
	$royal = get_theme_mod( 'effect_studio_royal', '#4a00a5' );
	$amber = get_theme_mod( 'effect_studio_amber', '#ffaa00' );

	$css = sprintf(
		':root{--color-royal:%1$s;--color-amber:%2$s;}',
		esc_attr( $royal ),
		esc_attr( $amber )
	);
	wp_add_inline_style( 'effect-studio-style', $css );
}
add_action( 'wp_enqueue_scripts', 'effect_studio_customize_css', 20 );

/**
 * جایگزینی شماره تلفن از تنظیمات.
 */
function effect_studio_filter_phone( $default ) {
	$phone = get_theme_mod( 'effect_studio_phone', $default );
	return $phone ? $phone : $default;
}
add_filter( 'effect_studio_phone', 'effect_studio_filter_phone' );

/**
 * جایگزینی ایمیل از تنظیمات.
 */
function effect_studio_filter_email( $default ) {
	$email = get_theme_mod( 'effect_studio_email', $default );
	return $email ? $email : $default;
}
add_filter( 'effect_studio_email', 'effect_studio_filter_email' );
