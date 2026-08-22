import Layout from '../components/Layout';
import { pages } from '../lib/content';
import { getPage, isConfigured } from '../lib/wp';

export default function AboutUs({ data, connected }) {
  const d = data || pages['about-us'];
  return (
    <Layout connected={connected}>
      <section className="hero">
        <h1>{d.title}</h1>
        <p>{d.hero}</p>
        <div className="cta-row">
          <a className="btn btn-amber" href="/#contact">
            همکاری با ما
          </a>
        </div>
      </section>

      <section className="section">
        <div className="container">
          <h2>تیم حرفه‌ای و خلاق افکت</h2>
          <p className="lead">{d.body}</p>
        </div>
      </section>

      <section className="section section-alt">
        <div className="container">
          <h2>مفتخر به همکاری با بیش از ۱۰۰ استارتاپ و بیزنس‌های موفق</h2>
        </div>
      </section>
    </Layout>
  );
}

export async function getStaticProps() {
  const data = await getPage('about-us', pages['about-us']);
  return { props: { data, connected: isConfigured }, revalidate: 60 };
}
