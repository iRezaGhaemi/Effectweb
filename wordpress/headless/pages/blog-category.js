import Link from 'next/link';
import Layout from '../components/Layout';
import { pages, posts } from '../lib/content';
import { getPage, isConfigured } from '../lib/wp';

export default function BlogCategory({ data, connected }) {
  const d = data || pages['blog-category'];
  return (
    <Layout connected={connected}>
      <main className="flex min-h-screen w-full flex-col gap-16 bg-surface py-6">
        <section className="px-4 sm:px-[30px]">
          <h1 className="text-[30px] font-bold leading-[1.6] text-ink">{d.title}</h1>
          <p className="mt-2 text-[16px] text-muted-2">{d.hero}</p>
        </section>

        <section className="px-4 sm:px-[30px]">
          <h2 className="text-[24px] font-bold leading-snug text-ink sm:text-[28px]">داغ ترین مطالب این دسته</h2>
          <div className="mt-6 grid grid-cols-1 gap-6 md:grid-cols-3">
            {posts.map((p, i) => (
              <Link key={p.slug} href={`/post/${p.slug}`} className="contents">
                <article className="group flex cursor-pointer flex-col gap-3 rounded-2xl border border-line bg-white p-3 transition-all duration-300 hover:-translate-y-1.5 hover:shadow-xl">
                  <img src={`/images/blogthumb-${i % 6}.jpeg`} alt={p.title} className="h-[160px] w-full rounded-xl object-cover" loading="lazy" />
                  <h3 className="text-right text-[15px] font-semibold leading-7 text-ink">{p.title}</h3>
                </article>
              </Link>
            ))}
          </div>
        </section>
      </main>
    </Layout>
  );
}

export async function getStaticProps() {
  const data = await getPage('blog-category', pages['blog-category']);
  return { props: { data, connected: isConfigured }, revalidate: 60 };
}
