import Layout from '../../components/Layout';
import { products } from '../../lib/content';
import { getProducts, isConfigured } from '../../lib/wp';

export default function Product({ product, connected }) {
  if (!product) {
    return (
      <Layout connected={connected}>
        <section className="hero">
          <h1>محصول یافت نشد</h1>
        </section>
      </Layout>
    );
  }
  return (
    <Layout connected={connected}>
      <section className="hero">
        <h1>{product.title}</h1>
        <p>{product.desc}</p>
        <div className="cta-row">
          <a className="btn btn-amber" href="#">
            افزودن به سبد
          </a>
        </div>
      </section>

      <section className="section">
        <div className="container">
          <h2>توضیحات محصول</h2>
          <p className="lead">{product.desc}</p>
          <p className="price" style={{ color: 'var(--royal)', fontWeight: 700, fontSize: 18 }}>
            {product.price}
          </p>
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
