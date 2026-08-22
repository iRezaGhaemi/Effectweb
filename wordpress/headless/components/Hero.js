import Link from 'next/link';

/**
 * هیروی صفحات فرعی — با کلاس‌های Tailwind واقعی (هماهنگ با طراحی برند).
 */
export default function Hero({ title, subtitle, cta, ctaHref = '/#contact', cta2, cta2Href = '/#services' }) {
  return (
    <section className="px-3 pt-3 sm:px-[30px] sm:pt-6">
      <div className="bg-hero relative overflow-hidden rounded-[24px] sm:rounded-[29px]">
        <div className="relative z-10 mx-auto mt-16 max-w-[894px] px-6 text-center sm:mt-[82px]">
          <h1 className="mt-[26px] text-[30px] font-black leading-[1.35] text-white sm:text-[38px]">
            {title}
          </h1>
          {subtitle ? (
            <p className="mx-auto mt-[26px] max-w-[894px] text-[14px] font-medium leading-[30px] text-white/85 sm:text-[16px]">
              {subtitle}
            </p>
          ) : null}
          <div className="mt-[26px] flex flex-wrap items-center justify-center gap-3.5">
            {cta ? (
              <a href={ctaHref} className="flex h-11 items-center rounded-xl bg-amber px-7 text-[14.5px] text-ink-2 transition-colors hover:bg-amber-dark">
                {cta}
              </a>
            ) : null}
            {cta2 ? (
              <a href={cta2Href} className="flex h-11 items-center rounded-xl bg-royal-2 px-7 text-[14.5px] text-white transition-colors hover:bg-[#6d0ac0]">
                {cta2}
              </a>
            ) : null}
          </div>
        </div>
        <div className="relative z-10 mt-16 pb-9 sm:mt-[82px] sm:pb-[47px]" />
      </div>
    </section>
  );
}
