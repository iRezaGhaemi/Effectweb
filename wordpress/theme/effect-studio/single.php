<?php
/**
 * قالب نوشته‌ها.
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
		<div class="container entry-content">
			<header class="entry-header">
				<h1 class="page-title entry-title"><?php the_title(); ?></h1>
				<div class="entry-meta">
					<?php
					printf(
						/* translators: %s: تاریخ انتشار */
						esc_html__( 'انتشار: %s', 'effect-studio' ),
						'<time datetime="' . esc_attr( get_the_date( 'c' ) ) . '">' . esc_html( get_the_date() ) . '</time>'
					);
					?>
				</div>
			</header>

			<?php if ( has_post_thumbnail() ) : ?>
				<div class="post-thumbnail"><?php the_post_thumbnail( 'large' ); ?></div>
			<?php endif; ?>

			<div class="entry-body">
				<?php the_content(); ?>
			</div>
		</div>
	</article>
	<?php
endwhile;
?>

<?php
get_footer();
