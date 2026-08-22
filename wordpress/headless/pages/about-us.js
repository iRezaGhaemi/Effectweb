import Layout from '../components/Layout';
import { pages } from '../lib/content';
import { getPage, isConfigured } from '../lib/wp';

const TEAM = ['Reza Ghaemi', 'Reza Ghaemi', 'Reza Ghaemi', 'Reza Ghaemi', 'Reza Ghaemi'];
const TRUST = [
  'دارای نماد اعتماد الکترونیکی',
  'دارای مجوز رسمی از نظام صنفی رایانه ای',
  'عضو طلایی انجمن صنفی کسب و کار های اینترنتی',
  'شرکت خلاق, معاونت دانش بنیان ریاست جمهوری',
];

export default function AboutUs({ data, connected }) {
  const d = data || pages['about-us'];
  return (
    <Layout connected={connected}>
      <main className="flex min-h-screen w-full flex-col gap-24 bg-surface py-6">
        <section className="mx-auto flex w-full max-w-[1280px] flex-col gap-16 px-4 xl:px-0">
          {/* فرم تماس + اطلاعات تماس */}
          <div className="flex flex-col-reverse gap-6 lg:flex-row">
            <div className="order-2 flex w-full flex-col gap-3 lg:order-1 lg:w-[310px]">
              <div className="flex flex-1 flex-col justify-center gap-3 rounded-[20px] border border-line px-4 py-4">
                {TRUST.map((t) => (
                  <div key={t} className="flex items-center gap-2">
                    <span className="text-[11.5px] leading-5 text-ink-500">{t}</span>
                  </div>
                ))}
              </div>
              <a href="tel:+989153892088" className="flex h-[82px] items-center gap-3 rounded-[20px] border border-line px-4">
                <span className="flex h-12 w-12 shrink-0 items-center justify-center rounded-xl bg-[#FFAA00] text-white">☎</span>
                <span className="flex flex-col">
                  <span className="text-[13px] text-gray-450">پاسخگویی از ۹ صبح تا ۵ عصر</span>
                  <span dir="ltr" className="text-base font-semibold text-ink-600">۰۹۱۵ ۳۸۹ ۲۰۸۸</span>
                </span>
              </a>
            </div>

            <div className="order-1 flex flex-1 flex-col gap-6 rounded-[20px] border border-line p-6 lg:order-2">
              <div className="flex flex-col gap-2">
                <h3 className="text-[23px] font-semibold leading-10 text-ink-900">با ما در ارتباط باشید</h3>
                <p className="text-[19px] leading-10 text-gray-550">با انتخاب هر یک از راه های ارتباطی زیر از کارشناسان ما مشاوره رایگان دریافت کنید.</p>
              </div>
              <div className="grid gap-6 sm:grid-cols-3">
                <a href="tel:+989151234567" className="flex h-24 items-center gap-4 rounded-2xl bg-brand-100/70 px-5 transition-colors hover:bg-brand-100">
                  <span className="flex h-12 w-12 shrink-0 items-center justify-center rounded-full bg-white text-brand-700">☎</span>
                  <span className="flex min-w-0 flex-1 flex-col items-end text-right">
                    <span className="text-[19px] font-semibold leading-8 text-brand-700">موبایل</span>
                    <span className="max-w-full truncate text-base leading-7 text-brand-700">۹۸۹۱۵۱۲۳۴۵۶۷</span>
                  </span>
                </a>
                <a href="mailto:hello@effect.studio" className="flex h-24 items-center gap-4 rounded-2xl bg-brand-100/70 px-5 transition-colors hover:bg-brand-100">
                  <span className="flex h-12 w-12 shrink-0 items-center justify-center rounded-full bg-white text-brand-700">✉</span>
                  <span className="flex min-w-0 flex-1 flex-col items-end text-right">
                    <span className="text-[19px] font-semibold leading-8 text-brand-700">ایمیل</span>
                    <span className="max-w-full truncate text-base leading-7 text-brand-700">hello@effect.studio</span>
                  </span>
                </a>
                <a href="https://t.me/" className="flex h-24 items-center gap-4 rounded-2xl bg-brand-100/70 px-5 transition-colors hover:bg-brand-100">
                  <span className="flex h-12 w-12 shrink-0 items-center justify-center rounded-full bg-white text-brand-700">✈</span>
                  <span className="flex min-w-0 flex-1 flex-col items-end text-right">
                    <span className="text-[19px] font-semibold leading-8 text-brand-700">تلگرام</span>
                    <span className="max-w-full truncate text-base leading-7 text-brand-700">۹۸۹۱۵۱۲۳۴۵۶۷</span>
                  </span>
                </a>
              </div>
            </div>
          </div>

          {/* تیم */}
          <div className="flex flex-col gap-6">
            <div className="flex items-center justify-between">
              <div>
                <h2 className="text-[28px] font-bold text-ink-900">تیم حرفه ای و خلاق افکت</h2>
                <p className="text-[13px] font-light leading-6 text-gray-550">{d.body}</p>
              </div>
              <a href="#" className="shrink-0 text-[13px] text-brand-700 hover:underline">مشاهده همه</a>
            </div>
            <div className="grid grid-cols-2 gap-6 sm:grid-cols-3 lg:grid-cols-5">
              {TEAM.map((name, i) => (
                <article key={i} className="group relative flex h-[334px] flex-col justify-end overflow-hidden rounded-[20px] p-4">
                  <img alt={name} loading="lazy" className="object-cover transition-transform duration-500 group-hover:scale-105" style={{ position: 'absolute', height: '100%', width: '100%', left: 0, top: 0 }} src="/images/team-reza.png" />
                  <div className="pointer-events-none absolute inset-x-0 bottom-0 h-1/2 bg-gradient-to-t from-black/70 via-black/25 to-transparent" />
                  <div className="relative flex flex-col items-start gap-0.5 text-right">
                    <span className="text-base font-semibold leading-8 text-[#FAFAFA]">{name}</span>
                    <span className="text-[11px] leading-5 text-[#FAFAFA]">Product Design Lead</span>
                    <div className="mt-1 flex items-center gap-1.5">
                      <span className="flex h-8 items-center rounded-lg bg-[#FFAA00]/10 px-2 py-1.5"><span className="text-[11px] leading-5 text-amber-600">Product</span></span>
                      <span className="flex h-8 items-center rounded-lg bg-[#FFAA00]/10 px-2 py-1.5"><span className="text-[11px] leading-5 text-amber-600">Ui</span></span>
                    </div>
                  </div>
                </article>
              ))}
            </div>
          </div>

          {/* آمار */}
          <div className="flex flex-col items-center gap-3 rounded-[20px] border border-line p-8 text-center">
            <h2 className="text-[22px] font-bold text-ink-900">مفتخر به همکاری با بیش از ۱۰۰ استارتاپ و بیزنس های موفق</h2>
          </div>
        </section>
      </main>
    </Layout>
  );
}

export async function getStaticProps() {
  const data = await getPage('about-us', pages['about-us']);
  return { props: { data, connected: isConfigured }, revalidate: 60 };
}
