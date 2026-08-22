import Layout from '../../components/Layout';
import { posts } from '../../lib/content';
import { getPost, getPosts, isConfigured } from '../../lib/wp';

const PARAGRAPHS = [
  'نسل جدید هیوندای الانترا از نسخه بهینه شده زبان طراحی هنر فولاد (Art of Steel) پیروی می‌کند.',
  'برندهای کره‌ای به ایجاد تغییرات گسترده ظاهری هنگام معرفی نسل جدید خودروهایشان شهرت دارند. نسل هشتم هیوندای الانترا نیز با ظاهری کاملاً متفاوت نسبت به نسل فعلی، اکنون در نمایشگاه خودرو بوسان ۲۰۲۶ معرفی شده است.',
  'هیوندای الانترا جدید از گلگیرهای برجسته و دستگیره‌های درب مخفی‌شونده هم‌سطح با بدنه بهره می‌برد. نسل هشتم الانترا بزرگتر از نسل قبلی است.',
  'هیوندای ادعا می‌کند که سدان کوچک الانترا، اکنون ابعاد مشابهی با برادر بزرگترش یعنی هیوندای سوناتا دارد. نسل جدید الانترا علاوه بر طول، ۳۰ میلی‌متر عریض‌تر شده و عرض آن به ۱۸۵۵ میلی‌متر می‌رسد.',
  'فضای داخلی الانترا اکنون به کلاس بالاتر خود یعنی سوناتا شبیه شده است. این خودرو از نسل جدید سیستم اطلاعات سرگرمی پلیوس (Pleos)، مبتنی بر اندروید بهره می‌برد. صفحه نمایشگر لمسی استاندارد این خودرو ۱۲.۹ اینچی است.',
  'کلاستر (پشت‌آمپر) دیجیتالی کوچک و افقی روی داشبورد و در خط دید راننده قرار گرفته است. لوگو هیوندای روی غربیلک فرمان حذف شده و به جای لوگو سنتی، چهار نقطه قرار گرفته‌اند که حرف H انگلیسی را تداعی می‌کند.',
];

export default function Post({ post, connected }) {
  if (!post) {
    return (
      <Layout connected={connected}>
        <main className="flex min-h-screen w-full flex-col gap-16 bg-surface py-6">
          <h1 className="px-4 text-[30px] font-bold text-ink">نوشته یافت نشد</h1>
        </main>
      </Layout>
    );
  }
  const bodyText = post.body && post.body !== post.excerpt ? null : PARAGRAPHS;

  return (
    <Layout connected={connected}>
      <main className="flex min-h-screen w-full flex-col gap-16 bg-surface py-6">
        {/* هیرو مقاله */}
        <section className="px-4 sm:px-[30px]">
          <div className="mx-auto max-w-[860px]">
            <div className="flex items-center gap-2 text-[13px] text-muted">
              <span>رضا قائمی</span>
              <span className="h-3 w-px bg-line" />
              <span>{post.date || '۳ ساعت قبل'}</span>
            </div>
            <h1 className="mt-4 text-[28px] font-bold leading-[1.6] text-ink sm:text-[34px]">{post.title}</h1>
            <img src="/images/blogthumb-4.webp" alt={post.title} className="mt-6 h-[320px] w-full rounded-2xl object-cover" loading="lazy" />
          </div>
        </section>

        {/* بدنه مقاله */}
        <section className="px-4 sm:px-[30px]">
          <article className="mx-auto max-w-[860px]">
            <h2 className="text-[22px] font-bold leading-8 text-ink">تغییرات گسترده در نسل جدید هیوندای الانترا</h2>
            {bodyText
              ? bodyText.slice(0, 4).map((t, i) => (
                  <p key={i} className="mt-4 text-right text-[15px] leading-8 text-body">{t}</p>
                ))
              : (
                  <div className="mt-4 text-right text-[15px] leading-8 text-body" dangerouslySetInnerHTML={{ __html: post.body }} />
                )}

            <h2 className="mt-10 text-[22px] font-bold leading-8 text-ink">هیوندای الانترا جدید عضلانی‌تر می‌شود</h2>
            {bodyText
              ? bodyText.slice(4).map((t, i) => (
                  <p key={i} className="mt-4 text-right text-[15px] leading-8 text-body">{t}</p>
                ))
              : null}
          </article>
        </section>

        {/* تازه‌های تکنولوژی */}
        <section className="px-4 sm:px-[30px]">
          <div className="mx-auto max-w-[860px]">
            <h2 className="text-[22px] font-bold leading-8 text-ink">تازه های تکنولوژی</h2>
            <div className="mt-4 rounded-2xl border border-line bg-white p-4">
              <p className="text-[14px] leading-7 text-body">پیلار کلاستر چیست؟ استراتژی هوشمندانه برای افزایش ترافیک و بهبود سئو</p>
            </div>
          </div>
        </section>
      </main>
    </Layout>
  );
}

export async function getStaticPaths() {
  const list = await getPosts(posts);
  const paths = list.map((p) => ({ params: { slug: p.slug } }));
  return { paths, fallback: 'blocking' };
}

export async function getStaticProps({ params }) {
  const list = await getPosts(posts);
  const fallback = list.find((p) => p.slug === params.slug) || null;
  const post = await getPost(params.slug, fallback);
  return { props: { post, connected: isConfigured }, revalidate: 60 };
}
