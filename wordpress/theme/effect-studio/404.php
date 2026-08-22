<?php
/**
 * قالب صفحه ۴۰۴.
 *
 * @package Effect_Studio
 */

get_header();
?>

<div class="container entry-content" style="text-align:center;padding-top:80px;padding-bottom:80px;">
	<h1 class="page-title" style="font-size:56px;color:var(--color-royal);"><?php esc_html_e( '۴۰۴', 'effect-studio' ); ?></h1>
	<p style="font-size:18px;"><?php esc_html_e( 'صفحه‌ای که دنبال آن هستید پیدا نشد.', 'effect-studio' ); ?></p>
	<a href="<?php echo esc_url( home_url( '/' ) ); ?>" style="display:inline-flex;height:48px;align-items:center;padding:0 24px;border-radius:12px;background:var(--color-amber);color:var(--color-ink);font-weight:600;">
		<?php esc_html_e( 'بازگشت به صفحه اصلی', 'effect-studio' ); ?>
	</a>
</div>

<?php
get_footer();
