import Marquee from './Marquee';

const TESTIMONIALS = [
  { name: 'فرهاد محمدی', role: 'مدیرعامل شرکت قطع', text: 'لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ، و با استفاده از طراحان گرافیک است، چاپگرها و متون بلکه روزنامه و مجله در ستون و سطرآنچنان که لازم است، و برای شرایط فعلی تکنولوژی مورد نیاز، و کاربردهای متنوع با هدف بهبود ابزارهای کاربردی می باشد.' },
  { name: 'فرهاد محمدی', role: 'مدیرعامل شرکت قطع', text: 'لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ، و با استفاده از طراحان گرافیک است، چاپگرها و متون بلکه روزنامه و مجله در ستون و سطرآنچنان که لازم است، و برای شرایط فعلی تکنولوژی مورد نیاز، و کاربردهای متنوع با هدف بهبود ابزارهای کاربردی می باشد.' },
  { name: 'فرهاد محمدی', role: 'مدیرعامل شرکت قطع', text: 'لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ، و با استفاده از طراحان گرافیک است، چاپگرها و متون بلکه روزنامه و مجله در ستون و سطرآنچنان که لازم است، و برای شرایط فعلی تکنولوژی مورد نیاز، و کاربردهای متنوع با هدف بهبود ابزارهای کاربردی می باشد.' },
  { name: 'فرهاد محمدی', role: 'مدیرعامل شرکت قطع', text: 'لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ، و با استفاده از طراحان گرافیک است، چاپگرها و متون بلکه روزنامه و مجله در ستون و سطرآنچنان که لازم است، و برای شرایط فعلی تکنولوژی مورد نیاز، و کاربردهای متنوع با هدف بهبود ابزارهای کاربردی می باشد.' },
];

export default function Testimonials() {
  return (
    <section className="mt-24">
      <div className="mx-auto max-w-[1280px] px-6">
        <div>
          <h2 className="flex items-center gap-3 text-[24px] font-extrabold leading-snug text-ink sm:text-[28px]">
            همراهان ما درباره افکت می‌گوین
          </h2>
          <p className="mt-2 text-[16px] text-muted-2">TESTIMONIAL</p>
        </div>
      </div>
      <div className="mx-auto mt-10 max-w-[1280px] px-6">
        <Marquee className="py-1">
          <div className="animate-marquee-slow flex w-max items-stretch gap-6">
            {TESTIMONIALS.map((t, i) => (
              <article key={i} dir="rtl" className="flex w-[300px] shrink-0 flex-col gap-6 rounded-[24px] border border-line bg-white p-6">
                <div className="flex items-center gap-3">
                  <div className="size-[68px] shrink-0 rounded-xl object-cover bg-mist" />
                  <div className="text-right">
                    <h3 className="text-[16px] font-semibold text-ink">{t.name}</h3>
                    <p className="mt-1.5 text-[13px] text-muted-2">{t.role}</p>
                  </div>
                </div>
                <p className="text-right text-[12.5px] leading-7 text-soft sm:text-[13px]">{t.text}</p>
              </article>
            ))}
          </div>
        </Marquee>
      </div>
    </section>
  );
}
