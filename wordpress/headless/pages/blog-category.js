import Link from 'next/link';
import Layout from '../components/Layout';
import Hero from '../components/Hero';
import { pages, posts } from '../lib/content';
import { getPage, isConfigured } from '../lib/wp';

export default function BlogCategory({ data, connected }) {
  const d = data || pages['blog-category'];
  return (
    <Layout connected={connected}>
      <Hero title={d.title} subtitle={d.hero} />

      <section className="mt-24 scroll-mt-8">
        <div className="mx-auto w-full max-w-[1280px] px-6">
          <h2 className="flex items-center gap-3 text-[24px] font-extrabold leading-snug text-ink sm:text-[28px]">
            داغ‌ترین مطالب این دسته
          </h2>
          <div className="mx-auto mt-10 grid max-w-[1280px] grid-cols-1 gap-6 md:grid-cols-3">
            {posts.map((p) => (
              <Link key={p.slug} href={`/post/${p.slug}`} className="group rounded-[20px] border border-line bg-panel p-3 transition-shadow hover:shadow-xl">
                <h3 className="mt-3 text-right text-[15.5px] font-semibold leading-8 text-body transition-colors group-hover:text-royal">{p.title}</h3>
              </Link>
            ))}
          </div>
        </div>
      </section>
    </Layout>
  );
}

export async function getStaticProps() {
  const data = await getPage('blog-category', pages['blog-category']);
  return { props: { data, connected: isConfigured }, revalidate: 60 };
}
