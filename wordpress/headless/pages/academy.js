import Link from 'next/link';
import Layout from '../components/Layout';
import { pages } from '../lib/content';
import { getPage, isConfigured } from '../lib/wp';

export default function Academy({ data, connected }) {
  const d = data || pages.academy;
  const courses = d.courses || pages.academy.courses;
  return (
    <Layout connected={connected}>
      <section className="hero">
        <h1>{d.hero || pages.academy.hero}</h1>
        <p>{d.body}</p>
        <div className="cta-row">
          <a className="btn btn-amber" href="/academy#courses">
            مشاهده دوره‌ها
          </a>
        </div>
      </section>

      <section className="section" id="courses">
        <div className="container">
          <h2>دسته‌بندی دوره‌ها</h2>
          <div className="cards">
            {courses.map((c) => (
              <Link href="/course" className="card" key={c.title}>
                <h3>{c.title}</h3>
                <p>{c.desc}</p>
              </Link>
            ))}
          </div>
        </div>
      </section>
    </Layout>
  );
}

export async function getStaticProps() {
  const data = await getPage('academy', pages.academy);
  return { props: { data, connected: isConfigured }, revalidate: 60 };
}
