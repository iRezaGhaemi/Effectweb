import Link from 'next/link';
import Layout from '../components/Layout';
import { posts } from '../lib/content';
import { getPosts, isConfigured } from '../lib/wp';

export default function Blog({ list, connected }) {
  return (
    <Layout connected={connected}>
      <section className="hero">
        <h1>بلاگ استودیو اثر</h1>
        <p>آخرین مقالات، ویدئوها و اخبار دنیای تکنولوژی و طراحی.</p>
      </section>

      <section className="section">
        <div className="container">
          <h2>تازه‌های روز</h2>
          <div className="cards">
            {list.map((p) => (
              <Link href={`/post/${p.slug}`} className="card" key={p.slug}>
                <h3>{p.title}</h3>
                <p>{p.excerpt}</p>
                <p className="meta">{p.date}</p>
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
