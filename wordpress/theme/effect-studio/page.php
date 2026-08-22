<?php
/**
 * قالب برگه‌ها.
 *
 * @package Effect_Studio
 */

get_header();
?>

<?php
while ( have_posts() ) :
	the_post();
	?>
	<article id="post-<?php the_ID(); ?>" <?php post_class(); ?>>
		<div class="entry-content">
			<?php effect_studio_the_page_content(); ?>
		</div>
	</article>
	<?php
endwhile;
?>

<?php
get_footer();
