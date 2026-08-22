<?php
/**
 * الگوی «محتوایی یافت نشد».
 *
 * @package Effect_Studio
 */
?>

<section class="no-results not-found">
	<header class="page-header">
		<h1 class="page-title"><?php esc_html_e( 'چیزی یافت نشد', 'effect-studio' ); ?></h1>
	</header>

	<div class="page-content">
		<?php if ( is_home() && current_user_can( 'publish_posts' ) ) : ?>
			<p>
				<?php
				printf(
					/* translators: %s: لینک نوشتن نوشته */
					wp_kses( __( 'آماده انتشار اولین نوشته هستید؟ <a href="%s">از اینجا شروع کنید</a>.', 'effect-studio' ), array( 'a' => array( 'href' => array() ) ) ),
					esc_url( admin_url( 'post-new.php' ) )
				);
				?>
			</p>
		<?php elseif ( is_search() ) : ?>
			<p><?php esc_html_e( 'نتیجه‌ای برای جستجوی شما پیدا نشد. عبارت دیگری را امتحان کنید.', 'effect-studio' ); ?></p>
			<?php get_search_form(); ?>
		<?php else : ?>
			<p><?php esc_html_e( 'به نظر می‌رسد چیزی در این مکان پیدا نمی‌شود.', 'effect-studio' ); ?></p>
			<?php get_search_form(); ?>
		<?php endif; ?>
	</div>
</section>
