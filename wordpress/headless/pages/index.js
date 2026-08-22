import Link from 'next/link';
import Layout from '../components/Layout';
import { home, posts } from '../lib/content';
import { getPage, getPosts, isConfigured } from '../lib/wp';

const SERVICE_IMAGES = {
  'سوشال مدیا': '/images/service-soshial.jpeg',
  مارکتینگ: '/images/service-marketing.jpeg',
  'سئو': '/images/service-seo.jpeg',
  'تبلیغات': '/images/service-ads.jpeg',
  'هویت بصری': '/images/service-identity.jpeg',
  'طراحی سایت و اپلیکیشن': '/images/service-web.jpeg',
};

const SERVICE_EN = {
  'سوشال مدیا': 'Social Media',
  مارکتینگ: 'Marketing',
  'سئو': 'SEO',
  'تبلیغات': 'ADS',
  'هویت بصری': 'Identity',
  'طراحی سایت و اپلیکیشن': 'Web Design',
};

export default function Home({ data, latestPosts, connected }) {
  const d = data || home;
  const services = d.services || home.services;

  return (
    <Layout connected={connected}>
      <section className="px-3 pt-3 sm:px-[30px] sm:pt-6">
        <div className="bg-hero relative overflow-hidden rounded-[24px] sm:rounded-[29px]">
          {/* هیرو */}
          <div className="relative z-10 mx-auto mt-16 max-w-[894px] px-6 text-center sm:mt-[82px]">
            <span className="inline-block rounded-full bg-gradient-to-b from-[#f000ff9e] to-transparent p-px">
              <span className="block rounded-full bg-[#1f01447d] px-7 py-3 text-[15px] leading-6 text-white sm:text-[16px]">
                استودیو اثــر
              </span>
            </span>
            <h1 className="mt-[26px] text-[30px] font-black leading-[1.35] text-white sm:text-[38px]">
              {d.hero?.title || 'هم مسیر تا تغییر'}
            </h1>
            <p className="mx-auto mt-[26px] max-w-[894px] text-[14px] font-medium leading-[30px] text-white/85 sm:text-[16px]">
              {d.hero?.subtitle ||
                'ما با ترکیب تخصص در طراحی محصول، طراحی گرافیک و تولید محتوا، راهکارهایی خلاقانه و مؤثر ارائه می‌دهیم تا برند شما متمایز، ماندگار و آینده‌نگر باشد.'}
            </p>
            <div className="mt-[26px] flex flex-wrap items-center justify-center gap-3.5">
              <a href="/#contact" className="flex h-11 items-center rounded-xl bg-royal-2 px-7 text-[14.5px] text-white transition-colors hover:bg-[#6d0ac0]">
                مشاوره پروژه
              </a>
              <a href="/#services" className="flex h-11 items-center rounded-xl bg-amber px-7 text-[14.5px] text-ink-2 transition-colors hover:bg-amber-dark">
                خدمات ما
              </a>
            </div>
          </div>

          {/* آمار + لوگوی مشتریان */}
          <div className="relative z-10 mt-16 pb-9 sm:mt-[82px] sm:pb-[47px]">
            <p className="px-6 text-center text-[15px] leading-8 text-white/90 sm:text-[18px]">
              {d.stats || 'مفتخر به همکاری با بیش از 100 استارتاپ و بیزنس های موفق'}
            </p>
            <div className="fade-x marquee-wrap scrollbar-hide mt-5 overflow-x-auto lg:mx-[92px]" dir="ltr">
              <div className="animate-marquee flex h-[94px] w-max items-center gap-8">
                {[0, 1, 2, 3, 4, 5].map((i) => (
                  <span key={i} className="animate-twinkle flex h-[94px] w-[143px] shrink-0 items-center justify-center">
                    <img src="/images/client-logo.webp" alt="" className="max-h-full max-w-full object-contain" loading="lazy" />
                  </span>
                ))}
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* خدمات */}
      <section id="services" className="mt-24 scroll-mt-8">
        <div className="mx-auto w-full max-w-[1280px] px-6">
          <div className="flex items-start justify-between gap-6">
            <div>
              <h2 className="flex items-center gap-3 text-[24px] font-extrabold leading-snug text-ink sm:text-[28px]">
                خدمات آژانس دیجیتال اثر
              </h2>
              <p className="mt-2 text-[16px] text-muted-2">SERVICES</p>
            </div>
          </div>
          <p className="mt-5 text-right text-[12.5px] leading-7 text-soft sm:text-[13px]">
            ما در آژانس دیجیتال مارکتینگ لین هر محتوا و فعالیتی که در فضای دیجیتال بازار ایران نیاز دارید را، با بالاترین سطح کیفیت به شما ارائه می‌دهیم، و شما را به مشتریانی می‌رسانیم که به دنبال آن خدمت هستند.
          </p>
        </div>

        <div className="mx-auto mt-10 grid max-w-[1280px] grid-cols-1 gap-6 px-6 md:grid-cols-2 xl:grid-cols-3">
          {services.map((name) => (
            <article
              key={name}
              className="group flex h-full flex-col gap-[18px] rounded-[20px] border border-line bg-panel p-3 transition-shadow hover:shadow-xl hover:shadow-royal/5"
            >
              <div className="flex items-start justify-between gap-4 px-1 pt-1">
                <div className="text-right">
                  <h3 className="text-[18px] font-bold text-ink">{name}</h3>
                  <p className="mt-1 text-[12.5px] text-muted">{SERVICE_EN[name] || ''}</p>
                </div>
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round" className="mt-1 text-ink transition-transform duration-300 group-hover:-translate-y-1 group-hover:translate-x-1" aria-hidden="true"><path d="M7 17 17 7" /><path d="M9 7h8v8" /></svg>
              </div>
              <p className="px-1 text-right text-[12.5px] leading-6 text-ink-2">
                {name === 'طراحی سایت و اپلیکیشن' && 'طراحی سایت حرفه‌ای تجربه کاربری بهتری را برای بازدیدکنندگان ایجاد می‌کند و برند شما را در دنیای آنلاین متمایز می‌کند.'}
                {name === 'هویت بصری' && 'با توجه به هویت برند کسب‌وکارتان لوگو، تایپوگرافی و آیکون‌گرافی خود را به ما بسپارید تا خدمات شما به روشی ساده و دیدنی معرفی شود.'}
                {name === 'سوشال مدیا' && 'ما با طراحی استراتژی‌های درست و بروز، تعاملات و محتوای شما را در شبکه‌های اجتماعی به بهترین حالت می‌رسانیم.'}
                {name === 'مارکتینگ' && 'با ابزارهای پیشرفته دیجیتال مارکتینگ، شما را به مشتریانی می‌رسانیم که به دنبال خدمات شما هستند.'}
                {name === 'سئو' && 'با بهینه‌سازی اصولی، جایگاه شما را در نتایج جستجو ارتقا می‌دهیم تا دیده شوید.'}
                {name === 'تبلیغات' && 'کمپین‌های تبلیغاتی هدفمند با بالاترین بازدهی برای رشد برند شما.'}
              </p>
              <img
                src={SERVICE_IMAGES[name] || '/images/client-logo.webp'}
                alt={name}
                className="mt-auto block h-[120px] w-full shrink-0 rounded-2xl object-cover"
                loading="lazy"
              />
            </article>
          ))}
        </div>
      </section>

      {/* چرا اثر + آخرین مقالات */}
      <section className="bg-dots-light mt-24 py-16">
        <div className="mx-auto max-w-[1280px] px-6">
          <h2 className="text-center text-[22px] font-extrabold leading-snug text-ink sm:text-[27px]">چرا اثر را انتخاب کنیم؟</h2>
          <p className="mx-auto mt-4 max-w-[720px] text-center text-[14px] leading-8 text-body">{home.why}</p>
        </div>
      </section>

      <section className="mt-24 scroll-mt-8">
        <div className="mx-auto max-w-[1280px] px-6">
          <h2 className="text-right text-[20px] font-semibold text-ink sm:text-[23px]">آخرین مقالات و ویدئوها</h2>
          <div className="mt-6 grid grid-cols-1 gap-6 md:grid-cols-3">
            {latestPosts.slice(0, 3).map((p) => (
              <Link key={p.slug} href={`/post/${p.slug}`} className="group rounded-[20px] border border-line bg-panel p-3 transition-shadow hover:shadow-xl">
                <h3 className="mt-3 text-right text-[15.5px] font-semibold leading-8 text-body transition-colors group-hover:text-royal">{p.title}</h3>
                <p className="text-right text-[12.5px] text-muted">{p.date}</p>
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
  return { props: { data, latestPosts, connected: isConfigured }, revalidate: 60 };
}
