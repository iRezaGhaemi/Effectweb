<?php
/**
 * Template Name: پیکسل‌پرفکت (فایل HTML اصلی)
 *
 * این قالب صفحه، فایل HTML اصلی سایت را به‌صورت خام خروجی می‌دهد تا
 * نتیجه ۱۰۰٪ پیکسل‌پرفکت باشد. فایل HTML بر اساس اسلاگ صفحه از پوشه
 * `frozen/` قالب خوانده می‌شود.
 *
 * نقشه اسلاگ -> فایل (در پوشه frozen/):
 *   home         -> effect-studio.html
 *   about-us     -> effect-studio-about-us.html
 *   academy      -> effect-studio-academy.html
 *   course       -> effect-studio-course.html
 *   blog         -> effect-studio-blog.html
 *   blog-category-> effect-studio-category.html
 *   sample-post  -> effect-studio-post.html
 *   shop         -> effect-studio-shop.html
 *   pegboard     -> effect-studio-product.html
 *
 * @package Effect_Studio
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

$slug = get_post_field( 'post_name', get_the_ID() );

$map = array(
	'home'          => 'effect-studio.html',
	'about-us'      => 'effect-studio-about-us.html',
	'academy'       => 'effect-studio-academy.html',
	'course'        => 'effect-studio-course.html',
	'blog'          => 'effect-studio-blog.html',
	'blog-category' => 'effect-studio-category.html',
	'sample-post'   => 'effect-studio-post.html',
	'shop'          => 'effect-studio-shop.html',
	'pegboard'      => 'effect-studio-product.html',
);

$file = '';
if ( isset( $map[ $slug ] ) ) {
	$file = get_template_directory() . '/frozen/' . $map[ $slug ];
}

if ( $file && file_exists( $file ) ) {
	header( 'Content-Type: text/html; charset=UTF-8' );
	readfile( $file );
	exit;
}

// اگر فایل HTML یافت نشد، یک پیام راهنما نمایش بده.
get_header();
?>
<div class="container entry-content" style="padding-top:60px;padding-bottom:60px;">
	<h1 style="color:var(--color-royal);"><?php esc_html_e( 'فایل HTML این صفحه یافت نشد', 'effect-studio' ); ?></h1>
	<p><?php esc_html_e( 'فایل‌های پیکسل‌پرفکت را در پوشه frozen/ قالب قرار دهید. برای جزئیات، راهنمای پکیج را ببینید.', 'effect-studio' ); ?></p>
</div>
<?php
get_footer();
