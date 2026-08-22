import Link from 'next/link';
import Layout from '../components/Layout';
import { pages, posts } from '../lib/content';
import { getPage, isConfigured } from '../lib/wp';

export default function BlogCategory({ data, connected }) {
  const d = data || pages['blog-category'];
  return (
    <Layout connected={connected}>
      <section className="hero">
        <h1>{d.title}</h1>
        <p>{d.hero}</p>
      </section>

      <section className="section">
        <div className="container">
          <h2>{d.body || 'داغ‌ترین مطالب این دسته'}</h2>
          <div className="cards">
            {posts.map((p) => (
              <Link href={`/post/${p.slug}`} className="card" key={p.slug}>
                <h3>{p.title}</h3>
                <p>{p.excerpt}</p>
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
