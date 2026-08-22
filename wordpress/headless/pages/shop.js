import Link from 'next/link';
import Layout from '../components/Layout';
import Hero from '../components/Hero';
import { products } from '../lib/content';
import { getProducts, isConfigured } from '../lib/wp';

export default function Shop({ list, connected }) {
  return (
    <Layout connected={connected}>
      <Hero title="محصولات با تخفیف استثنایی" subtitle="دوره‌های آموزشی، محصولات دیجیتال و پکیج‌های استودیو اثر." />

      <section className="mt-24 scroll-mt-8">
        <div className="mx-auto w-full max-w-[1280px] px-6">
          <h2 className="flex items-center gap-3 text-[24px] font-extrabold leading-snug text-ink sm:text-[28px]">
            محصولات
          </h2>
          <div className="mx-auto mt-10 grid max-w-[1280px] grid-cols-1 gap-6 md:grid-cols-3">
            {list.map((p) => (
              <Link key={p.slug} href={`/product/${p.slug}`} className="group rounded-[20px] border border-line bg-panel p-3 transition-shadow hover:shadow-xl">
                <img src="/images/product-pegboard.jpeg" alt={p.title} className="block h-[160px] w-full rounded-2xl object-cover" loading="lazy" />
                <h3 className="mt-3 text-right text-[16px] font-semibold leading-8 text-ink">{p.title}</h3>
                <p className="text-right text-[13px] leading-6 text-ink-2">{p.desc}</p>
                <p className="mt-2 text-right text-[16px] font-bold text-royal">{p.price}</p>
              </Link>
            ))}
          </div>
        </div>
      </section>
    </Layout>
  );
}

export async function getStaticProps() {
  const list = await getProducts(products);
  return { props: { list, connected: isConfigured }, revalidate: 60 };
}
