/**
 * بخش «چرا اثر را انتخاب کنیم؟» — با انیمیشن‌های عمودی
 * animate-why-up / animate-why-down (دقیقاً مثل HTML اصلی).
 */
const COLUMNS = [
  { speed: '18s', anim: 'animate-why-down', items: ['هویت برند متمایز', 'پشتیبانی سریع و کارآمد', 'مشاوره تخصصی و بروز'] },
  { speed: '22s', anim: 'animate-why-down', items: ['تلفیق خلاقیت و استراتژی', 'تیم تخصصی و حرفه‌ای', 'تجربه کاربری در اولویت'] },
  { speed: '20s', anim: 'animate-why-up', items: ['طراحی یکپارچه و چند بعدی', 'راهکارهای اختصاصی برای هر کسب‌وکار', 'ارائه گزارشات روند پروژه'] },
];

function Item({ text }) {
  return (
    <div className="flex h-[93px] items-center justify-start gap-4 rounded-[23px] border border-why-line bg-why-pill pe-2 ps-5">
      <span className="flex size-[58px] shrink-0 items-center justify-center rounded-[13px] bg-gradient-to-br from-[#25005500] to-[#5100bb99]" />
      <span className="text-[15px] leading-7 text-white">{text}</span>
    </div>
  );
}

function Spacer() {
  return (
    <div
      className="h-[93px] rounded-[23px] border border-transparent"
      style={{
        background: 'linear-gradient(180deg, #1b0629 0%, rgba(27,6,41,0) 100%)',
        borderColor: 'rgba(45,9,93,0.5)',
      }}
      aria-hidden="true"
    />
  );
}

export default function WhySection() {
  return (
    <div className="relative mt-12">
      <div className="grid grid-cols-1 gap-[11px] sm:grid-cols-2 xl:grid-cols-3">
        {COLUMNS.map((col) => (
          <div key={col.speed} className="why-col fade-y relative h-[405px] overflow-hidden">
            <div className={`flex flex-col gap-[11px] ${col.anim}`} style={{ '--why-speed': col.speed }}>
              {/* برای حلقه بینهایت، آیتم‌ها دو بار تکرار می‌شوند */}
              {[...col.items, ...col.items, ...col.items].map((text, i) =>
                i % (col.items.length + 1) === col.items.length ? (
                  <Spacer key={i} />
                ) : (
                  <Item key={i} text={text} />
                )
              )}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
