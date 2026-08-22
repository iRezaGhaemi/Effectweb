<?php
/**
 * فوتر قالب.
 *
 * @package Effect_Studio
 */
?>
	</main><!-- #primary -->

	<footer id="colophon" class="site-footer">
		<div class="footer-cols">
			<div class="footer-col">
				<h4><?php esc_html_e( 'خدمات اثر', 'effect-studio' ); ?></h4>
				<?php
				$services = array(
					__( 'طراحی سایت و اپلیکیشن', 'effect-studio' ),
					__( 'هویت بصری', 'effect-studio' ),
					__( 'سوشال مدیا', 'effect-studio' ),
					__( 'مارکتینگ و سئو', 'effect-studio' ),
				);
				foreach ( $services as $service ) :
					?>
					<a href="<?php echo esc_url( home_url( '/#services' ) ); ?>"><?php echo esc_html( $service ); ?></a><br>
				<?php endforeach; ?>
			</div>

			<div class="footer-col">
				<h4><?php esc_html_e( 'دسترسی آسان', 'effect-studio' ); ?></h4>
				<?php
				$quick_links = array(
					__( 'صفحه اصلی', 'effect-studio' )    => home_url( '/' ),
					__( 'فروشگاه', 'effect-studio' )       => home_url( '/shop/' ),
					__( 'مقالات', 'effect-studio' )        => home_url( '/blog/' ),
					__( 'ارتباط با ما', 'effect-studio' )  => home_url( '/#contact' ),
				);
				foreach ( $quick_links as $label => $url ) :
					?>
					<a href="<?php echo esc_url( $url ); ?>"><?php echo esc_html( $label ); ?></a><br>
				<?php endforeach; ?>
			</div>

			<div class="footer-col">
				<h4><?php esc_html_e( 'آکادمی اثر', 'effect-studio' ); ?></h4>
				<a href="<?php echo esc_url( home_url( '/academy/' ) ); ?>"><?php esc_html_e( 'دوره‌های آموزشی', 'effect-studio' ); ?></a><br>
				<a href="<?php echo esc_url( home_url( '/blog/' ) ); ?>"><?php esc_html_e( 'مقالات آموزشی', 'effect-studio' ); ?></a><br>
			</div>

			<div class="footer-col footer-contact">
				<h4><?php esc_html_e( 'ارتباط با ما', 'effect-studio' ); ?></h4>
				<p class="phone" dir="ltr"><?php echo esc_html( effect_studio_phone() ); ?></p>
				<p><?php echo esc_html( effect_studio_email() ); ?></p>
				<div class="footer-social">
					<?php effect_studio_social_icons(); ?>
				</div>
			</div>
		</div>

		<div class="footer-bottom">
			<p class="copyright"><?php esc_html_e( 'تمام حقوق برای استودیو اثر محفوظ می‌باشد.', 'effect-studio' ); ?></p>
			<p class="copyright" dir="ltr"><?php esc_html_e( 'All rights are reserved  |  ', 'effect-studio' ); ?><span class="amber">Effect Studio 2025</span></p>
		</div>
	</footer>
</div><!-- #page -->

<?php wp_footer(); ?>
</body>
</html>
