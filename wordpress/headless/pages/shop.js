import Link from 'next/link';
import Layout from '../components/Layout';
import { products } from '../lib/content';
import { getProducts, isConfigured } from '../lib/wp';

const PRODUCT_IMGS = ['/images/shop-0.jpeg', '/images/shop-1.jpeg', '/images/shop-2.jpeg'];

export default function Shop({ list, connected }) {
  return (
    <Layout connected={connected}>
      <main className="flex min-h-screen w-full flex-col gap-16 bg-surface py-6">
        {/* هیرو فروشگاه */}
        <section className="px-4 sm:px-[30px]">
          <div className="bg-hero relative overflow-hidden rounded-[24px] sm:rounded-[29px] p-8 sm:p-12">
            <div className="relative z-10 max-w-[640px]">
              <h1 className="text-[30px] font-bold leading-[1.6] text-panel min-[1900px]:text-[33px]">محصولات با تخفیف استثنایی</h1>
              <p className="mt-4 text-[16px] leading-8 text-panel">
                اگر شهری که دوست داری رو نتونستی از بین تابلوهای وبسایت پیدا کنی، روی دکمه افزودن به سبد خرید کلیک کن و اسم شهر مورد نظرت رو در باکس باز شده واسمون بنویس و سفارشت رو نهایی کن.
              </p>
              <a href="#products" className="mt-8 flex h-12 w-[123px] items-center justify-center rounded-xl bg-amber text-[16px] leading-8 text-ink transition-colors hover:bg-amber-dark">
                ثبت سفارش
              </a>
            </div>
          </div>
        </section>

        {/* محصولات */}
        <section id="products" className="px-4 sm:px-[30px]">
          <h2 className="text-[24px] font-bold leading-snug text-ink sm:text-[28px]">محصولات</h2>
          <div className="mt-6 grid grid-cols-1 gap-6 md:grid-cols-3">
            {list.map((p, i) => (
              <Link key={p.slug} href={`/product/${p.slug}`} className="contents">
                <article className="group flex flex-col gap-3 rounded-[20px] border border-line bg-white p-3 transition-all duration-300 hover:-translate-y-1.5 hover:shadow-xl">
                  <img src={PRODUCT_IMGS[i % PRODUCT_IMGS.length]} alt={p.title} className="h-[200px] w-full rounded-2xl object-cover transition-transform duration-500 group-hover:scale-105" loading="lazy" />
                  <div className="flex items-center justify-start gap-1.5">
                    <span className="flex h-6 items-center rounded-lg px-1.5 text-[11px] leading-5 bg-royal/10 text-royal">کتاب</span>
                    <span className="flex h-6 items-center rounded-lg px-1.5 text-[11px] leading-5 bg-[#ff7b06]/10 text-[#f95e00]">تخفیف ویژه</span>
                  </div>
                  <h3 className="text-right text-[16px] font-bold leading-8 text-body">{p.title}</h3>
                  <div className="flex items-center justify-start gap-1">
                    <span className="text-[16px] font-semibold leading-8 text-royal">{p.price.replace(' تومان', '')}</span>
                    <span className="text-[13px] leading-6 text-muted">تومان</span>
                  </div>
                  <button type="button" className="flex h-8 items-center gap-3 whitespace-nowrap rounded-lg px-3 text-[13px] leading-6 text-royal transition-colors hover:bg-royal/5">
                    افزودن به سبد خرید
                  </button>
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
  const list = await getProducts(products);
  return { props: { list, connected: isConfigured }, revalidate: 60 };
}
