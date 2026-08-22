<?php
/**
 * قالب صفحات ووکامرس (فروشگاه، دسته‌بندی، محصول و ...).
 *
 * @package Effect_Studio
 */

get_header();
?>

<div class="container entry-content">
	<?php
	woocommerce_content();
	?>
</div>

<?php
get_footer();
