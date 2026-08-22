import Layout from '../../components/Layout';
import { posts } from '../../lib/content';
import { getPost, getPosts, isConfigured } from '../../lib/wp';

export default function Post({ post, connected }) {
  if (!post) {
    return (
      <Layout connected={connected}>
        <section className="hero">
          <h1>نوشته یافت نشد</h1>
        </section>
      </Layout>
    );
  }
  return (
    <Layout connected={connected}>
      <section className="hero">
        <h1>{post.title}</h1>
        {post.date ? <p>{post.date}</p> : null}
      </section>
      <article className="container">
        <div
          className="prose"
          dangerouslySetInnerHTML={{ __html: post.body || post.excerpt }}
        />
      </article>
    </Layout>
  );
}

export async function getStaticPaths() {
  // اگر وردپرس متصل باشد، اسلاگ‌ها از آن می‌آیند؛ وگرنه از fallback.
  const list = await getPosts(posts);
  const paths = list.map((p) => ({ params: { slug: p.slug } }));
  return { paths, fallback: 'blocking' };
}

export async function getStaticProps({ params }) {
  const list = await getPosts(posts);
  const fallback = list.find((p) => p.slug === params.slug) || null;
  const post = await getPost(params.slug, fallback);
  return { props: { post, connected: isConfigured }, revalidate: 60 };
}
