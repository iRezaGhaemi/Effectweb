import Marquee from './Marquee';

const PORTFOLIO = [
  { img: '/images/portfolio-0.jpeg', tag: 'تیزر' },
  { img: '/images/portfolio-1.jpeg', tag: 'ریل' },
  { img: '/images/portfolio-2.jpeg', tag: 'ریل' },
  { img: '/images/portfolio-3.jpeg', tag: 'ریل' },
  { img: '/images/portfolio-4.jpeg', tag: 'ریل' },
  { img: '/images/portfolio-5.jpeg', tag: 'تیزر' },
  { img: '/images/portfolio-1.jpeg', tag: 'ریل' },
  { img: '/images/portfolio-2.jpeg', tag: 'ریل' },
  { img: '/images/portfolio-3.jpeg', tag: 'ریل' },
  { img: '/images/portfolio-4.jpeg', tag: 'ریل' },
];

const TABS = ['محتوا ویدئویی', 'عکاسی محصول', 'وبسایت'];
const FILTERS = ['همه', 'ریل اینستاگرام', 'تیزر تبلیغاتی', 'موشن', 'انیمیشن', 'هوش مصنوعی'];

export default function Portfolio() {
  return (
    <section className="mt-24">
      <div className="mx-auto max-w-[1280px] px-6">
        <div>
          <h2 className="flex items-center gap-3 text-[24px] font-extrabold leading-snug text-ink sm:text-[28px]">
            نمونه کار های استودیو افکت
          </h2>
          <p className="mt-2 text-[16px] text-muted-2">PORTFOLIO</p>
        </div>

        <div className="mt-5 flex flex-col items-start gap-4">
          <div className="flex rounded-xl bg-panel p-1.5 shadow-sm" role="tablist">
            {TABS.map((t, i) => (
              <button
                key={t}
                role="tab"
                aria-selected={i === 0}
                className={`rounded-lg px-4 py-2 text-[13px] transition-colors sm:px-6 sm:py-2.5 ${
                  i === 0 ? 'bg-[#f0f1f3] text-body' : 'text-muted hover:text-body'
                }`}
              >
                {t}
              </button>
            ))}
          </div>
          <div className="flex flex-wrap justify-end gap-2">
            {FILTERS.map((f, i) => (
              <button
                key={f}
                className={`rounded-lg px-4 py-2.5 text-[11px] transition-colors ${
                  i === 0 ? 'bg-royal/10 text-royal' : 'bg-[#5d5d5d1a] text-body hover:bg-[#5d5d5d2b]'
                }`}
              >
                {f}
              </button>
            ))}
          </div>
        </div>
      </div>

      <div className="mx-auto mt-10 max-w-[1280px] px-6">
        <Marquee className="ms-[calc(50%-50vw)] pb-2 pt-1">
          <div className="animate-pf-scroll flex w-max gap-4 sm:gap-6">
            {PORTFOLIO.map((p, i) => (
              <article
                key={i}
                dir="rtl"
                className="group relative h-[300px] shrink-0 overflow-hidden rounded-2xl sm:h-[394px] w-[84vw] sm:w-[600px]"
              >
                <img
                  src={p.img}
                  alt={p.tag}
                  className="absolute inset-0 h-full w-full object-cover transition-transform duration-500 group-hover:scale-105"
                  loading="lazy"
                />
                <div className="absolute inset-x-0 bottom-0 h-1/3 bg-gradient-to-t from-black/45 to-transparent" />
                <span className="glass-chip absolute right-4 top-4 rounded-lg px-3 py-1.5 text-[11px] text-white">
                  {p.tag}
                </span>
              </article>
            ))}
          </div>
        </Marquee>
      </div>
    </section>
  );
}
