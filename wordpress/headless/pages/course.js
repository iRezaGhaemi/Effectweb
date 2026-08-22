import Layout from '../components/Layout';
import { pages } from '../lib/content';
import { getPage, isConfigured } from '../lib/wp';

export default function Course({ data, connected }) {
  const d = data || pages.course;
  return (
    <Layout connected={connected}>
      <section className="hero">
        <h1>{d.title}</h1>
        <p>{d.hero}</p>
        <div className="cta-row">
          <a className="btn btn-amber" href="/course#curriculum">
            ثبت‌نام در دوره
          </a>
        </div>
      </section>

      <section className="section">
        <div className="container">
          <h2>توضیحات دوره</h2>
          <p className="lead">{d.body}</p>
        </div>
      </section>

      <section className="section section-alt" id="curriculum">
        <div className="container">
          <h2>آنچه در این دوره خواهید دید</h2>
          <p className="lead">{d.curriculum}</p>
        </div>
      </section>
    </Layout>
  );
}

export async function getStaticProps() {
  const data = await getPage('course', pages.course);
  return { props: { data, connected: isConfigured }, revalidate: 60 };
}
