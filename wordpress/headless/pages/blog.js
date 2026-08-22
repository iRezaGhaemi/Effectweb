import Link from 'next/link';
import Layout from '../components/Layout';
import { posts } from '../lib/content';
import { getPosts, isConfigured } from '../lib/wp';

const THUMBS = [
  '/images/blogthumb-0.jpeg',
  '/images/blogthumb-1.jpeg',
  '/images/blogthumb-2.jpeg',
  '/images/blogthumb-3.jpeg',
  '/images/blogthumb-4.webp',
  '/images/blogthumb-5.jpeg',
];

export default function Blog({ list, connected }) {
  return (
    <Layout connected={connected}>
      <main className="flex min-h-screen w-full flex-col gap-24 bg-surface py-6">
        {/* کارت‌های ویژه (داغ) */}
        <section className="px-4 sm:px-[30px]">
          <div className="grid grid-cols-1 gap-6 md:grid-cols-2 xl:grid-cols-[2.16fr_1fr_1fr]">
            {list.slice(0, 3).map((p, i) => (
              <Link
                key={p.slug}
                href={`/post/${p.slug}`}
                className={`contents`}
              >
                <article
                  className={`group relative flex cursor-pointer flex-col justify-between overflow-hidden rounded-2xl transition-all duration-300 hover:-translate-y-1.5 ${
                    i === 0 ? 'min-h-[420px] md:col-span-2 xl:col-span-1 xl:min-h-0' : 'min-h-[420px]'
                  }`}
                >
                  <img
                    src={THUMBS[i % THUMBS.length]}
                    alt={p.title}
                    className="absolute inset-0 h-full w-full object-cover transition-transform duration-700 ease-out group-hover:scale-105"
                    loading="lazy"
                  />
                  <div className="relative flex items-start justify-between p-6">
                    <span className="flex h-8 items-center gap-2 rounded-lg bg-[#5d5d5d]/10 px-1.5 py-1 text-[11px] text-panel backdrop-blur-md">
                      <span className="size-6 rounded-full bg-white/30" />
                      <span>رضا قائمی</span>
                      <span className="h-3 w-px bg-[#e0e2e7]/50" aria-hidden="true" />
                      <span>۳ ساعت قبل</span>
                    </span>
                  </div>
                  <div className="relative flex flex-col gap-2 p-6 pt-0">
                    <h2 className="text-[18px] font-bold leading-8 text-white">{p.title}</h2>
                  </div>
                </article>
              </Link>
            ))}
          </div>
        </section>

        {/* تازه‌های روز */}
        <section className="mt-24">
          <div className="px-4 sm:px-[30px]">
            <div className="flex items-start justify-between gap-6">
              <div>
                <h2 className="flex items-center gap-3 text-[24px] font-bold leading-snug text-ink sm:text-[28px]">
                  تازه های روز
                </h2>
                <p className="mt-2 text-[16px] text-muted-2 sm:text-[19px]">News of the day</p>
              </div>
              <div className="flex h-16 w-40 shrink-0 items-center rounded-[32px] bg-panel p-2" dir="ltr">
                <button type="button" aria-label="نمای لیستی" className="flex h-12 w-16 items-center justify-center">
                  <span className="flex h-12 w-16 items-center justify-center rounded-xl transition-colors">☰</span>
                </button>
                <button type="button" aria-label="نمای گریدی" className="flex h-12 w-16 items-center justify-center">
                  <span className="flex h-12 w-16 items-center justify-center rounded-xl transition-colors bg-[#f0f1f3]">⊞</span>
                </button>
              </div>
            </div>
            <div className="mt-6 flex items-center justify-start gap-2" role="tablist" aria-label="فیلتر موضوع">
              <button type="button" role="tab" aria-selected="true" className="flex h-9 items-center rounded-lg px-3 text-[11px] leading-5 transition-colors bg-royal/25 text-royal ring-1 ring-royal">هوش مصنوعی</button>
              <button type="button" role="tab" aria-selected="false" className="flex h-9 items-center rounded-lg px-3 text-[11px] leading-5 transition-colors bg-royal/10 text-royal hover:bg-royal/20">برچسب</button>
              <button type="button" role="tab" aria-selected="false" className="flex h-9 items-center rounded-lg px-3 text-[11px] leading-5 transition-colors bg-royal/10 text-royal hover:bg-royal/20">برچسب</button>
            </div>
          </div>

          <div className="mt-8 grid grid-cols-1 gap-6 px-4 sm:px-[30px] md:grid-cols-2 xl:grid-cols-3">
            {list.map((p, i) => (
              <Link key={p.slug} href={`/post/${p.slug}`} className="contents">
                <article className="group flex cursor-pointer flex-col gap-3 rounded-2xl border border-line bg-white p-3 transition-all duration-300 hover:-translate-y-1.5 hover:shadow-xl">
                  <img src={THUMBS[i % THUMBS.length]} alt={p.title} className="h-[180px] w-full rounded-xl object-cover transition-transform duration-700 group-hover:scale-105" loading="lazy" />
                  <h3 className="text-right text-[15px] font-semibold leading-7 text-ink">{p.title}</h3>
                  <p className="text-right text-[12px] leading-6 text-muted">{p.date}</p>
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
  const list = await getPosts(posts);
  return { props: { list, connected: isConfigured }, revalidate: 60 };
}
