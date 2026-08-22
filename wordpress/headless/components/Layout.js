import Link from 'next/link';
import { useRouter } from 'next/router';
import { brand, nav } from '../lib/content';

/**
 * هدر و فوتر با کلاس‌های دقیق HTML اصلی (۱۰۰٪ مطابق طراحی).
 * محتوا (منو، تلفن، لوگو) از وردپرس/fallback خوانده می‌شود.
 */
export default function Layout({ children, connected }) {
  const router = useRouter();

  return (
    <>
      <header className="relative z-30 px-4 pt-6 sm:px-10 sm:pt-[47px] xl:px-20">
        <div className="flex items-center justify-between gap-4">
          <Link href="/" aria-label="استودیو اثر" className="shrink-0">
            <img
              src="/images/logo.webp"
              alt="استودیو اثر"
              className="w-[108px] h-auto select-none sm:w-[130px]"
              draggable="false"
            />
          </Link>

          <div className="hidden min-w-0 flex-1 items-center justify-center gap-6 lg:flex">
            <nav className="flex items-center gap-6 text-[15px] xl:gap-8">
              <Link href="/" className="py-2 transition-colors hover:text-white text-lilac">
                استودیو اثر
              </Link>
              <Link href="/about-us" className="py-2 transition-colors hover:text-white text-panel">
                درباره ما
              </Link>
              <a href="/#services" className="py-2 transition-colors hover:text-white text-panel">
                خدمات اثر
              </a>
              <Link href="/blog" className="py-2 transition-colors hover:text-white text-panel">
                بلاگ
              </Link>
              <Link href="/shop" className="py-2 transition-colors hover:text-white text-panel">
                فروشگاه
              </Link>
              <a href="/#contact" className="py-2 transition-colors hover:text-white text-panel">
                ارتباط با ما
              </a>
            </nav>

            <span className="hidden 2xl:block h-[26px] w-px shrink-0 bg-[#e0e2e7]" aria-hidden="true" />
            <Link
              href="/academy"
              className="hidden h-12 shrink-0 items-center gap-3 rounded-xl bg-amber px-5 text-[15px] text-ink transition-colors hover:bg-amber-dark 2xl:flex"
            >
              آکادمی هوش مصنوعی
            </Link>
          </div>

          <div className="flex items-center gap-5">
            <div className="hidden items-center gap-4 md:flex">
              <span className="flex size-12 shrink-0 items-center justify-center rounded-2xl bg-amber text-ink">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true"><path d="M5.2 4h3.4l1.6 4-2.3 1.8a13.5 13.5 0 0 0 6.3 6.3l1.8-2.3 4 1.6v3.4c0 1-.8 1.9-1.9 1.8C10.5 20 4 13.5 3.3 5.9 3.2 4.9 4.1 4 5.2 4Z" /></svg>
              </span>
              <span className="text-start leading-tight">
                <span className="block text-[12px] text-muted">۹ صبح تا ۵ عصر</span>
                <span className="mt-1 block text-[15px] font-semibold tracking-wide text-panel">{brand.phone}</span>
              </span>
            </div>

            <span className="hidden 2xl:block h-[26px] w-px shrink-0 bg-[#e0e2e7]" aria-hidden="true" />
            <a href="/#contact" className="hidden h-12 items-center gap-3 rounded-xl bg-royal px-5 text-[15px] text-panel transition-colors hover:bg-royal-2 md:flex">
              ثبت نام | ورود
            </a>

            <button className="flex size-11 items-center justify-center rounded-xl bg-white/10 text-white lg:hidden" aria-label="منو">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.7" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16" /></svg>
            </button>
          </div>
        </div>
      </header>

      <main>{children}</main>

      <footer className="mt-24 px-3 pb-3 sm:px-[30px] sm:pb-6">
        <div className="bg-footer relative overflow-hidden rounded-[24px] bg-[#1d0140] px-6 pb-6 pt-12 sm:rounded-[29px] sm:px-10 sm:pb-10">
          <div className="mx-auto grid max-w-[1280px] grid-cols-1 gap-8 md:grid-cols-2 xl:grid-cols-4">
            <div>
              <h3 className="px-2 text-[16px] font-medium leading-7 text-white">خدمات اثر</h3>
              <a href="/#services" className="flex h-8 items-center rounded-lg px-2 text-[13px] text-[#d0d0d2] transition-colors hover:bg-white/5 hover:text-white">طراحی سایت و اپلیکیشن</a>
              <a href="/#services" className="flex h-8 items-center rounded-lg px-2 text-[13px] text-[#d0d0d2] transition-colors hover:bg-white/5 hover:text-white">هویت بصری</a>
              <a href="/#services" className="flex h-8 items-center rounded-lg px-2 text-[13px] text-[#d0d0d2] transition-colors hover:bg-white/5 hover:text-white">سوشال مدیا</a>
              <a href="/#services" className="flex h-8 items-center rounded-lg px-2 text-[13px] text-[#d0d0d2] transition-colors hover:bg-white/5 hover:text-white">مارکتینگ و سئو</a>
            </div>
            <div>
              <h3 className="px-2 text-[16px] font-medium leading-7 text-white">دسترسی آسان</h3>
              <Link href="/" className="flex h-8 items-center rounded-lg px-2 text-[13px] text-[#d0d0d2] transition-colors hover:bg-white/5 hover:text-white">صفحه اصلی</Link>
              <Link href="/shop" className="flex h-8 items-center rounded-lg px-2 text-[13px] text-[#d0d0d2] transition-colors hover:bg-white/5 hover:text-white">فروشگاه</Link>
              <Link href="/blog" className="flex h-8 items-center rounded-lg px-2 text-[13px] text-[#d0d0d2] transition-colors hover:bg-white/5 hover:text-white">مقالات</Link>
              <a href="/#contact" className="flex h-8 items-center rounded-lg px-2 text-[13px] text-[#d0d0d2] transition-colors hover:bg-white/5 hover:text-white">ارتباط با ما</a>
            </div>
            <div>
              <h3 className="px-2 text-[16px] font-medium leading-7 text-white">آکادمی اثر</h3>
              <Link href="/academy" className="flex h-8 items-center rounded-lg px-2 text-[13px] text-[#d0d0d2] transition-colors hover:bg-white/5 hover:text-white">دوره‌های آموزشی</Link>
              <Link href="/blog" className="flex h-8 items-center rounded-lg px-2 text-[13px] text-[#d0d0d2] transition-colors hover:bg-white/5 hover:text-white">مقالات آموزشی</Link>
            </div>
            <div>
              <h3 className="px-2 text-[16px] font-medium leading-7 text-white">ارتباط با ما</h3>
              <p dir="ltr" className="px-2 text-right text-[20px] font-semibold text-[#FFAA00]">{brand.phone}</p>
              <p className="px-2 text-[13px] text-[#d0d0d2]">{brand.email}</p>
            </div>
          </div>
          <div className="mx-auto mt-8 max-w-[1280px] border-t border-[#430096] pt-6">
            <p className="text-[14px] text-white">تمام حقوق برای استودیو اثر محفوظ می‌باشد.</p>
            <p dir="ltr" className="text-[14px] text-white">All rights are reserved | <span className="font-medium text-amber">Effect Studio 2025</span></p>
          </div>
        </div>
      </footer>

      <div className={`conn-badge ${connected ? 'ok' : ''}`}>
        {connected ? '● متصل به وردپرس' : '○ حالت پیش‌نمایش (بدون وردپرس)'}
      </div>
    </>
  );
}
