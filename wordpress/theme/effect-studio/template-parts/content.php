<?php
/**
 * الگوی نمایش یک آیتم محتوا (پیش‌فرض).
 *
 * @package Effect_Studio
 */
?>

<article id="post-<?php the_ID(); ?>" <?php post_class(); ?>>
	<header class="entry-header">
		<?php
		if ( is_singular() ) {
			the_title( '<h1 class="entry-title">', '</h1>' );
		} else {
			the_title( '<h2 class="entry-title"><a href="' . esc_url( get_permalink() ) . '" rel="bookmark">', '</a></h2>' );
		}
		?>
	</header>

	<?php if ( has_post_thumbnail() && ! is_singular() ) : ?>
		<a class="post-thumbnail" href="<?php the_permalink(); ?>"><?php the_post_thumbnail( 'medium_large' ); ?></a>
	<?php endif; ?>

	<div class="entry-summary">
		<?php the_excerpt(); ?>
	</div>
</article>
