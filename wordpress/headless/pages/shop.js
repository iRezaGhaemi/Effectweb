import Link from 'next/link';
import Layout from '../components/Layout';
import { products } from '../lib/content';
import { getProducts, isConfigured } from '../lib/wp';

export default function Shop({ list, connected }) {
  return (
    <Layout connected={connected}>
      <section className="hero">
        <h1>محصولات با تخفیف استثنایی</h1>
        <p>دوره‌های آموزشی، محصولات دیجیتال و پکیج‌های استودیو اثر.</p>
      </section>

      <section className="section">
        <div className="container">
          <h2>محصولات</h2>
          <div className="cards">
            {list.map((p) => (
              <Link href={`/product/${p.slug}`} className="card" key={p.slug}>
                <h3>{p.title}</h3>
                <p>{p.desc}</p>
                <p className="price">{p.price}</p>
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
