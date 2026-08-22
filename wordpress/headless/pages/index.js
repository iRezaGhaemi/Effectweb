import Link from 'next/link';
import Layout from '../components/Layout';
import { home, posts } from '../lib/content';
import { getPage, getPosts, isConfigured } from '../lib/wp';

export default function Home({ data, latestPosts, connected }) {
  const d = data || home;
  return (
    <Layout connected={connected}>
      <section className="hero">
        <h1>{d.hero?.title || home.hero.title}</h1>
        <p>{d.hero?.subtitle || home.hero.subtitle}</p>
        <div className="cta-row">
          <a className="btn btn-amber" href={d.hero?.cta?.href || '/#contact'}>
            {d.hero?.cta?.label || 'مشاوره رایگان'}
          </a>
          <a className="btn btn-royal" href="/#services">
            مشاهده خدمات
          </a>
        </div>
      </section>

      <section className="section" id="services">
        <div className="container">
          <h2>خدمات آژانس دیجیتال اثر</h2>
          <p className="lead">
            طراحی سایت و اپلیکیشن، هویت بصری، سوشال مدیا، مارکتینگ، سئو و تبلیغات —
            راهکارهای اختصاصی برای هر کسب‌وکار.
          </p>
          <div className="services-grid">
            {(d.services || home.services).map((s) => (
              <div className="service-card" key={s}>
                {s}
              </div>
            ))}
          </div>
        </div>
      </section>

      <section className="section section-alt">
        <div className="container">
          <h2>{d.stats || home.stats}</h2>
        </div>
      </section>

      <section className="section">
        <div className="container">
          <h2>چرا اثر را انتخاب کنیم؟</h2>
          <p className="lead">{home.why}</p>
        </div>
      </section>

      <section className="section section-alt" id="contact">
        <div className="container">
          <h2>آخرین مقالات و ویدئوها</h2>
          <div className="cards">
            {latestPosts.slice(0, 3).map((p) => (
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
  const data = await getPage('home', home);
  const latestPosts = await getPosts(posts);
  return {
    props: { data, latestPosts, connected: isConfigured },
    revalidate: 60,
  };
}
