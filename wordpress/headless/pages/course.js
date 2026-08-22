import Layout from '../components/Layout';
import Hero from '../components/Hero';
import { pages } from '../lib/content';
import { getPage, isConfigured } from '../lib/wp';

export default function Course({ data, connected }) {
  const d = data || pages.course;
  return (
    <Layout connected={connected}>
      <Hero title={d.title} subtitle={d.hero} cta="ثبت‌نام در دوره" ctaHref="/course#curriculum" />

      <section className="mt-24 scroll-mt-8">
        <div className="mx-auto w-full max-w-[1280px] px-6">
          <h2 className="flex items-center gap-3 text-[24px] font-extrabold leading-snug text-ink sm:text-[28px]">
            توضیحات دوره
          </h2>
          <p className="mt-5 text-right text-[14px] leading-8 text-body">{d.body}</p>
        </div>
      </section>

      <section id="curriculum" className="bg-dots-light mt-24 py-16">
        <div className="mx-auto max-w-[1280px] px-6">
          <h2 className="text-[22px] font-extrabold leading-snug text-ink sm:text-[27px]">
            آنچه در این دوره خواهید دید
          </h2>
          <p className="mt-4 text-right text-[14px] leading-8 text-body">{d.curriculum}</p>
        </div>
      </section>
    </Layout>
  );
}

export async function getStaticProps() {
  const data = await getPage('course', pages.course);
  return { props: { data, connected: isConfigured }, revalidate: 60 };
}
