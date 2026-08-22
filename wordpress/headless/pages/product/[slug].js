import Layout from '../../components/Layout';
import { products } from '../../lib/content';
import { getProducts, isConfigured } from '../../lib/wp';

export default function Product({ product, connected }) {
  if (!product) {
    return (
      <Layout connected={connected}>
        <main className="flex min-h-screen w-full flex-col gap-16 bg-surface py-6">
          <h1 className="px-4 text-[30px] font-bold text-ink">محصول یافت نشد</h1>
        </main>
      </Layout>
    );
  }
  return (
    <Layout connected={connected}>
      <main className="flex min-h-screen w-full flex-col gap-16 bg-surface py-6">
        {/* هیرو محصول */}
        <section className="px-4 sm:px-[30px]">
          <div className="grid grid-cols-1 gap-8 lg:grid-cols-2">
            <div className="flex flex-col justify-center gap-4">
              <div className="flex items-center justify-start gap-1.5">
                <span className="flex h-6 items-center rounded-lg px-1.5 text-[11px] leading-5 bg-royal/10 text-royal">کتاب</span>
                <span className="flex h-6 items-center rounded-lg px-1.5 text-[11px] leading-5 bg-[#ff7b06]/10 text-[#f95e00]">تخفیف ویژه</span>
              </div>
              <h1 className="text-[30px] font-bold leading-[1.6] text-ink">{product.title}</h1>
              <p className="text-[16px] leading-8 text-body">{product.desc}</p>
              <div className="flex items-center justify-start gap-1">
                <span className="text-[24px] font-semibold leading-8 text-royal">{product.price.replace(' تومان', '')}</span>
                <span className="text-[14px] leading-6 text-muted">تومان</span>
              </div>
              <div className="flex items-center gap-3">
                <button type="button" className="flex h-12 items-center gap-3 rounded-xl bg-amber px-6 text-[15px] font-semibold text-ink transition-colors hover:bg-amber-dark">
                  افزودن به سبد خرید
                </button>
              </div>
            </div>
            <div className="relative h-[360px] overflow-hidden rounded-[20px] border border-line bg-white p-3">
              <img src="/images/prod-2.jpeg" alt={product.title} className="h-full w-full rounded-2xl object-cover" loading="lazy" />
            </div>
          </div>
        </section>

        {/* توضیحات */}
        <section className="px-4 sm:px-[30px]">
          <div className="rounded-[20px] border border-line bg-white p-6">
            <h2 className="text-[22px] font-bold leading-8 text-ink">توضیحات محصول</h2>
            <p className="mt-3 text-[14px] leading-8 text-body">{product.desc}</p>
          </div>
        </section>
      </main>
    </Layout>
  );
}

export async function getStaticPaths() {
  const list = await getProducts(products);
  const paths = list.map((p) => ({ params: { slug: p.slug } }));
  return { paths, fallback: 'blocking' };
}

export async function getStaticProps({ params }) {
  const list = await getProducts(products);
  const fallback = list.find((p) => p.slug === params.slug) || null;
  return { props: { product: fallback, connected: isConfigured }, revalidate: 60 };
}
