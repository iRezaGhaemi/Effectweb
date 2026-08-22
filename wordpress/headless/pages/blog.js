import Link from 'next/link';
import Layout from '../components/Layout';
import Hero from '../components/Hero';
import { posts } from '../lib/content';
import { getPosts, isConfigured } from '../lib/wp';

export default function Blog({ list, connected }) {
  return (
    <Layout connected={connected}>
      <Hero title="بلاگ استودیو اثر" subtitle="آخرین مقالات، ویدئوها و اخبار دنیای تکنولوژی و طراحی." />

      <section className="mt-24 scroll-mt-8">
        <div className="mx-auto w-full max-w-[1280px] px-6">
          <h2 className="flex items-center gap-3 text-[24px] font-extrabold leading-snug text-ink sm:text-[28px]">
            تازه‌های روز
          </h2>
          <div className="mx-auto mt-10 grid max-w-[1280px] grid-cols-1 gap-6 md:grid-cols-3">
            {list.map((p) => (
              <Link
                key={p.slug}
                href={`/post/${p.slug}`}
                className="group rounded-[20px] border border-line bg-panel p-3 transition-shadow hover:shadow-xl"
              >
                <h3 className="mt-3 text-right text-[15.5px] font-semibold leading-8 text-body transition-colors group-hover:text-royal">
                  {p.title}
                </h3>
                <p className="mt-2 text-right text-[12.5px] leading-6 text-muted">{p.excerpt}</p>
                <p className="mt-2 text-right text-[12px] text-muted">{p.date}</p>
              </Link>
            ))}
          </div>
        </div>
      </section>
    </Layout>
  );
}

export async function getStaticProps() {
  const list = await getPosts(posts);
  return { props: { list, connected: isConfigured }, revalidate: 60 };
}
