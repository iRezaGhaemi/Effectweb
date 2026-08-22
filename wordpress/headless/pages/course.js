import Layout from '../components/Layout';
import { pages } from '../lib/content';
import { getPage, isConfigured } from '../lib/wp';

export default function Course({ data, connected }) {
  const d = data || pages.course;
  return (
    <Layout connected={connected}>
      <main className="flex min-h-screen w-full flex-col gap-16 bg-surface py-6">
        {/* هیرو دوره */}
        <section className="mx-auto w-full max-w-[1280px] px-4 xl:px-0">
          <div className="flex flex-col items-center gap-6 text-center">
            <h1 className="text-[34px] font-bold leading-[1.3] text-ink-900">{d.title}</h1>
            <p className="max-w-[720px] text-base leading-8 text-body">{d.hero}</p>
            <div className="flex flex-wrap items-center justify-center gap-3">
              <a href="#curriculum" className="flex h-12 items-center rounded-xl bg-[#FFAA00] px-6 text-base text-[#181818] transition-opacity hover:opacity-90">
                ثبت‌نام در دوره
              </a>
            </div>
            <img src="/images/course-photoshop-intro.png" alt={d.title} className="mt-4 h-auto w-full max-w-[720px] rounded-[20px] object-cover" loading="lazy" />
          </div>
        </section>

        {/* توضیحات دوره */}
        <section className="mx-auto w-full max-w-[1280px] px-4 xl:px-0">
          <div className="flex flex-col gap-4 rounded-[20px] border border-line bg-white p-6">
            <h2 className="text-[24px] font-bold text-ink-900">توضیحات دوره</h2>
            <p className="text-[14px] leading-8 text-body">{d.body}</p>
          </div>
        </section>

        {/* سرفصل‌ها */}
        <section id="curriculum" className="mx-auto w-full max-w-[1280px] px-4 xl:px-0">
          <div className="flex flex-col gap-4 rounded-[20px] border border-line bg-white p-6">
            <h2 className="text-[24px] font-bold text-ink-900">آنچه در این دوره خواهید دید</h2>
            <p className="text-[14px] leading-8 text-body">{d.curriculum}</p>
          </div>
        </section>

        {/* گواهینامه */}
        <section className="mx-auto w-full max-w-[1280px] px-4 xl:px-0">
          <div className="flex flex-col items-center gap-6 rounded-[20px] border border-line bg-white p-8 text-center">
            <h2 className="text-[24px] font-bold text-ink-900">گواهینامه پایان دوره آکادمی اثر</h2>
            <img src="/images/course-certificate.png" alt="گواهینامه" className="h-auto w-full max-w-[420px] rounded-[16px] object-cover" loading="lazy" />
            <p className="text-[14px] leading-8 text-body">پس از پایان دوره، گواهینامه معتبر آکادمی اثر دریافت می‌کنید.</p>
          </div>
        </section>
      </main>
    </Layout>
  );
}

export async function getStaticProps() {
  const data = await getPage('course', pages.course);
  return { props: { data, connected: isConfigured }, revalidate: 60 };
}
