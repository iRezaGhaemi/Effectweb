import Layout from '../../components/Layout';
import { posts } from '../../lib/content';
import { getPost, getPosts, isConfigured } from '../../lib/wp';

export default function Post({ post, connected }) {
  if (!post) {
    return (
      <Layout connected={connected}>
        <section className="px-3 pt-3 sm:px-[30px] sm:pt-6">
          <div className="bg-hero relative overflow-hidden rounded-[24px] sm:rounded-[29px]">
            <h1 className="relative z-10 mx-auto max-w-[894px] px-6 pt-16 text-center text-[30px] font-black leading-[1.35] text-white sm:text-[38px]">
              نوشته یافت نشد
            </h1>
          </div>
        </section>
      </Layout>
    );
  }
  return (
    <Layout connected={connected}>
      <section className="px-3 pt-3 sm:px-[30px] sm:pt-6">
        <div className="bg-hero relative overflow-hidden rounded-[24px] sm:rounded-[29px]">
          <h1 className="relative z-10 mx-auto max-w-[894px] px-6 pt-16 text-center text-[30px] font-black leading-[1.35] text-white sm:text-[38px]">
            {post.title}
          </h1>
          {post.date ? (
            <p className="relative z-10 mx-auto max-w-[894px] px-6 pb-12 pt-4 text-center text-[14px] text-white/85">{post.date}</p>
          ) : null}
        </div>
      </section>
      <article className="mx-auto mt-10 max-w-[860px] px-6">
        <div
          className="text-right text-[15px] leading-8 text-body"
          dangerouslySetInnerHTML={{ __html: post.body || post.excerpt }}
        />
      </article>
    </Layout>
  );
}

export async function getStaticPaths() {
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
