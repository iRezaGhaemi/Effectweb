import Layout from '../components/Layout';
import Hero from '../components/Hero';
import { pages } from '../lib/content';
import { getPage, isConfigured } from '../lib/wp';

export default function AboutUs({ data, connected }) {
  const d = data || pages['about-us'];
  return (
    <Layout connected={connected}>
      <Hero title={d.title} subtitle={d.hero} cta="همکاری با ما" ctaHref="/#contact" />

      <section className="mt-24 scroll-mt-8">
        <div className="mx-auto w-full max-w-[1280px] px-6">
          <h2 className="flex items-center gap-3 text-[24px] font-extrabold leading-snug text-ink sm:text-[28px]">
            تیم حرفه‌ای و خلاق افکت
          </h2>
          <p className="mt-5 text-right text-[14px] leading-8 text-body">{d.body}</p>
        </div>
      </section>

      <section className="bg-dots-light mt-24 py-16">
        <div className="mx-auto max-w-[1280px] px-6">
          <h2 className="text-center text-[22px] font-extrabold leading-snug text-ink sm:text-[27px]">
            مفتخر به همکاری با بیش از ۱۰۰ استارتاپ و بیزنس‌های موفق
          </h2>
        </div>
      </section>
    </Layout>
  );
}

export async function getStaticProps() {
  const data = await getPage('about-us', pages['about-us']);
  return { props: { data, connected: isConfigured }, revalidate: 60 };
}
