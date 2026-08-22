import Link from 'next/link';
import Layout from '../components/Layout';
import { pages } from '../lib/content';
import { getPage, isConfigured } from '../lib/wp';

export default function Academy({ data, connected }) {
  const d = data || pages.academy;
  const courses = d.courses || pages.academy.courses;
  return (
    <Layout connected={connected}>
      <main className="flex min-h-screen w-full flex-col gap-24 bg-surface py-6">
        {/* هیرو + اسلایدر */}
        <section className="mx-auto w-full max-w-[1280px] px-4 xl:px-0">
          <div className="flex flex-col-reverse items-center gap-8 lg:flex-row">
            <div className="order-2 flex flex-col items-start gap-4 lg:order-1">
              <h1 className="text-[34px] font-bold leading-[1.3] text-ink-900">آموزش هدفمند, آینده ای روشن</h1>
              <p className="text-base leading-8 text-body">
                در دوره های آکادمی اثــر شما تنها یک ابزار آموزش نمی بینید، اصول و تفکر طراحی را با جدیدترین متدلوژی های آموزشی فرا خواهید گرفت تا بتوانید بهترین نسخه خود در بدو ورود به بازار کار باشید.
              </p>
              <a href="#courses" className="flex h-12 items-center rounded-xl bg-[#FFAA00] px-5 text-base text-[#181818] transition-opacity hover:opacity-90">
                مشاهده دوره ها
              </a>
            </div>
            <div className="relative order-1 h-[320px] w-[320px] shrink-0 sm:h-[420px] sm:w-[420px] lg:order-2 lg:h-[532px] lg:w-[532px]">
              <img alt="آکادمی اثر" className="object-contain" style={{ position: 'absolute', height: '100%', width: '100%' }} src="/images/course-cinema4d.png" />
            </div>
          </div>
          <div dir="ltr" className="relative mt-10 flex items-center justify-center gap-3">
            <button type="button" aria-label="قبلی" className="rotate-180 text-muted transition-colors hover:text-body">‹</button>
            <div className="flex items-center gap-1">
              <span className="h-[7px] w-[7px] rounded-full bg-line" />
              <span className="h-[7px] w-[27px] rounded-[5px] bg-royal" />
              <span className="h-[7px] w-[7px] rounded-full bg-line" />
              <span className="h-[7px] w-[7px] rounded-full bg-line" />
            </div>
            <button type="button" aria-label="بعدی" className="text-muted transition-colors hover:text-body">›</button>
          </div>
        </section>

        {/* دوره‌ها */}
        <section id="courses" className="mx-auto flex w-full max-w-[1280px] flex-col gap-12 px-4 xl:px-0">
          <div className="flex flex-col gap-4">
            <div className="flex flex-col-reverse items-start gap-4 sm:flex-row sm:items-end sm:justify-between">
              <label className="order-2 flex w-full flex-col gap-1 sm:w-[375px]">
                <span className="text-[13px] font-semibold leading-6 text-ink-900">جستجو</span>
                <span className="flex h-12 items-center gap-2 rounded-xl bg-[#FAFAFA] px-4">
                  <input placeholder="جستجو" className="w-full bg-transparent text-[13px] text-ink-900 outline-none placeholder:text-muted" />
                </span>
              </label>
              <div className="order-1 flex flex-col items-start gap-0 text-right">
                <h2 className="text-[28px] font-bold leading-[56px] text-ink-900">دسته بندی دوره ها</h2>
              </div>
            </div>
          </div>

          <div className="grid grid-cols-1 gap-6 md:grid-cols-2">
            {courses.map((c, i) => (
              <Link
                key={c.title}
                href="/course"
                className="group flex flex-col gap-4 rounded-[20px] border border-line bg-white p-5 transition-shadow hover:shadow-xl"
              >
                <img
                  src={i === 0 ? '/images/course-cinema4d.png' : '/images/course-photoshop.png'}
                  alt={c.title}
                  className="h-[200px] w-full rounded-2xl object-cover transition-transform duration-500 group-hover:scale-105"
                  loading="lazy"
                />
                <h3 className="text-[20px] font-bold text-ink-900">{c.title}</h3>
                <p className="text-[14px] leading-7 text-body">{c.desc}</p>
                <span className="text-[14px] font-semibold text-royal">مشاهده دوره ←</span>
              </Link>
            ))}
          </div>
        </section>
      </main>
    </Layout>
  );
}

export async function getStaticProps() {
  const data = await getPage('academy', pages.academy);
  return { props: { data, connected: isConfigured }, revalidate: 60 };
}
