<?php
/**
 * هدر قالب.
 *
 * @package Effect_Studio
 */
?>
<!doctype html>
<html <?php language_attributes(); ?>>
<head>
	<meta charset="<?php bloginfo( 'charset' ); ?>">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="profile" href="https://gmpg.org/xfn/11">
	<?php wp_head(); ?>
</head>
<body <?php body_class(); ?>>
<?php wp_body_open(); ?>

<div id="page" class="site">
	<a class="skip-link screen-reader-text" href="#primary"><?php esc_html_e( 'پرش به محتوا', 'effect-studio' ); ?></a>

	<header id="masthead" class="site-header">
		<div class="header-inner">
			<?php effect_studio_the_logo(); ?>

			<nav class="primary-nav" aria-label="<?php esc_attr_e( 'منوی اصلی', 'effect-studio' ); ?>">
				<?php
				wp_nav_menu(
					array(
						'theme_location' => 'primary',
						'menu_class'     => 'menu',
						'container'      => false,
						'fallback_cb'    => 'effect_studio_primary_menu_fallback',
					)
				);
				?>
			</nav>

			<div class="header-actions">
				<a class="academy-cta" href="<?php echo esc_url( effect_studio_academy_url() ); ?>">
					<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9.2 4.5A2.7 2.7 0 0 0 6.5 7.2c-1.6.5-2.7 2-2.7 3.8 0 1.4.7 2.6 1.8 3.3A3.4 3.4 0 0 0 9 20.6c.5 0 1-.1 1.5-.3V6a2.9 2.9 0 0 0-1.3-1.5Z"/><path d="M14.8 4.5a2.7 2.7 0 0 1 2.7 2.7c1.6.5 2.7 2 2.7 3.8 0 1.4-.7 2.6-1.8 3.3a3.4 3.4 0 0 1-3.4 6.3c-.5 0-1-.1-1.5-.3V6c.4-.9.8-1.3 1.3-1.5Z"/></svg>
					<?php esc_html_e( 'آکادمی هوش مصنوعی', 'effect-studio' ); ?>
				</a>

				<div class="header-phone">
					<span class="phone-icon">
						<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5.2 4h3.4l1.6 4-2.3 1.8a13.5 13.5 0 0 0 6.3 6.3l1.8-2.3 4 1.6v3.4c0 1-.8 1.9-1.9 1.8C10.5 20 4 13.5 3.3 5.9 3.2 4.9 4.1 4 5.2 4Z"/></svg>
					</span>
					<span>
						<span class="phone-label"><?php esc_html_e( '۹ صبح تا ۵ عصر', 'effect-studio' ); ?></span>
						<span class="phone-number" dir="ltr"><?php echo esc_html( effect_studio_phone() ); ?></span>
					</span>
				</div>

				<a class="login-btn" href="<?php echo esc_url( wp_login_url() ); ?>">
					<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="8" r="4"/><path d="M4.5 20.5c1.4-3.6 4.2-5.5 7.5-5.5s6.1 1.9 7.5 5.5"/></svg>
					<?php esc_html_e( 'ثبت نام | ورود', 'effect-studio' ); ?>
				</a>

				<button class="menu-toggle" aria-controls="mobile-nav" aria-expanded="false" aria-label="<?php esc_attr_e( 'منو', 'effect-studio' ); ?>">
					<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>
				</button>
			</div>
		</div>
	</header>

	<nav id="mobile-nav" class="mobile-nav" aria-label="<?php esc_attr_e( 'منوی موبایل', 'effect-studio' ); ?>">
		<?php
		wp_nav_menu(
			array(
				'theme_location' => 'primary',
				'menu_class'     => 'mobile-menu',
				'container'      => false,
				'fallback_cb'    => 'effect_studio_primary_menu_fallback',
			)
		);
		?>
	</nav>

	<main id="primary" class="site-main">
