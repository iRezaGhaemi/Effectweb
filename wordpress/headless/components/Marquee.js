import { useEffect, useRef } from 'react';

/**
 * کلون‌کننده‌ی marquee — محتوای داخل [data-clone] را برای حلقه بین‌هایت
 * دو برابر می‌کند (دقیقاً مثل اسکریپت اصلی سایت).
 */
export default function Marquee({ children, className = '', dir = 'ltr' }) {
  const ref = useRef(null);

  useEffect(() => {
    const el = ref.current;
    if (!el) return;
    const clone = () => {
      el.innerHTML += el.innerHTML;
      el.removeAttribute('data-clone');
    };
    const t1 = setTimeout(clone, 1200);
    const t2 = setTimeout(clone, 2600);
    return () => {
      clearTimeout(t1);
      clearTimeout(t2);
    };
  }, []);

  return (
    <div dir={dir} className={`fade-x marquee-wrap scrollbar-hide overflow-x-auto ${className}`}>
      <div data-clone="1" ref={ref} className="flex w-max items-center gap-8">
        {children}
      </div>
    </div>
  );
}
