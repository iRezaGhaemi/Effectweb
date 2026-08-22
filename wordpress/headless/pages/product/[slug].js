import Layout from '../../components/Layout';
import { products } from '../../lib/content';
import { getProducts, isConfigured } from '../../lib/wp';

export default function Product({ product, connected }) {
  if (!product) {
    return (
      <Layout connected={connected}>
        <section className="px-3 pt-3 sm:px-[30px] sm:pt-6">
          <div className="bg-hero relative overflow-hidden rounded-[24px] sm:rounded-[29px]">
            <h1 className="relative z-10 mx-auto max-w-[894px] px-6 pt-16 text-center text-[30px] font-black leading-[1.35] text-white sm:text-[38px]">
              محصول یافت نشد
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
            {product.title}
          </h1>
          <p className="relative z-10 mx-auto max-w-[894px] px-6 pb-12 pt-4 text-center text-[14px] text-white/85">{product.desc}</p>
        </div>
      </section>

      <section className="mt-10">
        <div className="mx-auto max-w-[860px] px-6">
          <img src="/images/product-pegboard.jpeg" alt={product.title} className="block h-auto w-full rounded-[20px] object-cover" loading="lazy" />
          <p className="mt-6 text-right text-[15px] leading-8 text-body">{product.desc}</p>
          <p className="mt-4 text-right text-[20px] font-bold text-royal">{product.price}</p>
          <a href="#" className="mt-6 flex h-12 items-center justify-center rounded-xl bg-amber px-7 text-[15px] font-semibold text-ink-2 transition-colors hover:bg-amber-dark">
            افزودن به سبد
          </a>
        </div>
      </section>
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
