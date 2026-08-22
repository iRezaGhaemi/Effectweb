import Link from 'next/link';
import { useRouter } from 'next/router';
import { brand, nav } from '../lib/content';

export default function Layout({ children, connected }) {
  const router = useRouter();

  return (
    <>
      <header className="site-header">
        <div className="header-inner">
          <Link href="/" className="brand">
            {brand.name} <span>|</span> {brand.tagline}
          </Link>
          <nav className="nav">
            {nav.map((item) => (
              <Link
                key={item.href}
                href={item.href}
                className={router.pathname === item.href ? 'active' : ''}
              >
                {item.label}
              </Link>
            ))}
          </nav>
          <span className="phone" dir="ltr">
            {brand.phone}
          </span>
        </div>
      </header>

      <main>{children}</main>

      <footer className="site-footer">
        <div className="footer-cols">
          <div>
            <h4>خدمات اثر</h4>
            <a href="/#services">طراحی سایت و اپلیکیشن</a>
            <br />
            <a href="/#services">هویت بصری</a>
            <br />
            <a href="/#services">سوشال مدیا</a>
            <br />
            <a href="/#services">مارکتینگ و سئو</a>
          </div>
          <div>
            <h4>دسترسی آسان</h4>
            <Link href="/">صفحه اصلی</Link>
            <br />
            <Link href="/shop">فروشگاه</Link>
            <br />
            <Link href="/blog">مقالات</Link>
            <br />
            <a href="/#contact">ارتباط با ما</a>
          </div>
          <div>
            <h4>آکادمی اثر</h4>
            <Link href="/academy">دوره‌های آموزشی</Link>
            <br />
            <Link href="/blog">مقالات آموزشی</Link>
          </div>
          <div>
            <h4>ارتباط با ما</h4>
            <p dir="ltr" style={{ color: 'var(--amber)', fontWeight: 700 }}>
              {brand.phone}
            </p>
            <p>{brand.email}</p>
          </div>
        </div>
        <div className="footer-bottom">
          <p>تمام حقوق برای استودیو اثر محفوظ می‌باشد.</p>
          <p dir="ltr">
            All rights are reserved | <span className="amber">Effect Studio 2025</span>
          </p>
        </div>
      </footer>

      <div className={`conn-badge ${connected ? 'ok' : ''}`}>
        {connected ? '● متصل به وردپرس' : '○ حالت پیش‌نمایش (بدون وردپرس)'}
      </div>
    </>
  );
}
