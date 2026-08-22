import Link from 'next/link';
import Layout from '../components/Layout';
import Hero from '../components/Hero';
import { pages } from '../lib/content';
import { getPage, isConfigured } from '../lib/wp';

export default function Academy({ data, connected }) {
  const d = data || pages.academy;
  const courses = d.courses || pages.academy.courses;
  return (
    <Layout connected={connected}>
      <Hero title={d.hero || pages.academy.hero} subtitle={d.body} cta="مشاهده دوره‌ها" ctaHref="/academy#courses" />

      <section id="courses" className="mt-24 scroll-mt-8">
        <div className="mx-auto w-full max-w-[1280px] px-6">
          <h2 className="flex items-center gap-3 text-[24px] font-extrabold leading-snug text-ink sm:text-[28px]">
            دسته‌بندی دوره‌ها
          </h2>
          <div className="mx-auto mt-10 grid max-w-[1280px] grid-cols-1 gap-6 md:grid-cols-2">
            {courses.map((c) => (
              <Link
                key={c.title}
                href="/course"
                className="group flex h-full flex-col gap-[18px] rounded-[20px] border border-line bg-panel p-4 transition-shadow hover:shadow-xl hover:shadow-royal/5"
              >
                <h3 className="text-[18px] font-bold text-ink">{c.title}</h3>
                <p className="text-[13px] leading-6 text-ink-2">{c.desc}</p>
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
