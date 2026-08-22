<?php
/**
 * قالب نتایج جستجو.
 *
 * @package Effect_Studio
 */

get_header();
?>

<div class="container entry-content">
	<header class="page-header">
		<h1 class="page-title">
			<?php
			/* translators: %s: عبارت جستجو */
			printf( esc_html__( 'نتایج جستجو برای: %s', 'effect-studio' ), '<span>' . get_search_query() . '</span>' );
			?>
		</h1>
	</header>

	<?php if ( have_posts() ) : ?>
		<?php
		while ( have_posts() ) :
			the_post();
			get_template_part( 'template-parts/content', 'search' );
		endwhile;

		the_posts_navigation();
		?>
	<?php else : ?>
		<?php get_template_part( 'template-parts/content', 'none' ); ?>
	<?php endif; ?>
</div>

<?php
get_footer();
