/**
 * توابع ارتباط با وردپرس از طریق REST API.
 *
 * اگر NEXT_PUBLIC_WP_URL تنظیم نشده باشد (یا درخواست ناموفق باشد)،
 * داده جایگزین (fallback) برگردانده می‌شود تا سایت همیشه رندر شود.
 */

const WP_URL = process.env.NEXT_PUBLIC_WP_URL || '';

async function wpFetch(path, fallback, revalidate = 60) {
  if (!WP_URL) return fallback;
  try {
    const res = await fetch(`${WP_URL}${path}`, {
      next: { revalidate },
      headers: { Accept: 'application/json' },
    });
    if (!res.ok) return fallback;
    return await res.json();
  } catch {
    return fallback;
  }
}

/**
 * خواندن یک برگه (Page) بر اساس اسلاگ.
 * فیلدهای ACF (در صورت وجود) روی آبجکت acf برگردانده می‌شوند و
 * در ساختار مورد انتظار کامپوننت‌ها نرمال‌سازی می‌شوند.
 */
export async function getPage(slug, fallback) {
  const data = await wpFetch(
    `/wp-json/wp/v2/pages?slug=${slug}&_embed`,
    null
  );
  if (Array.isArray(data) && data.length) {
    const p = data[0];
    const acf = p.acf || {};
    const out = { ...fallback, title: p.title?.rendered || fallback?.title };

    // صفحه اصلی: hero به‌صورت آبجکت (title/subtitle)
    if (acf.hero_title) out.hero = { ...(fallback?.hero || {}), title: acf.hero_title };
    if (acf.hero_subtitle) out.hero = { ...(out.hero || {}), subtitle: acf.hero_subtitle };

    // صفحات ساده: hero به‌صورت رشته متنی
    if (acf.hero_text) out.hero = acf.hero_text;

    if (acf.body) out.body = acf.body;
    if (acf.services) out.services = acf.services.map((s) => s.name);
    if (acf.stats) out.stats = acf.stats;
    if (acf.why) out.why = acf.why;
    if (acf.courses) out.courses = acf.courses.map((c) => ({ title: c.title, desc: c.desc }));
    if (acf.curriculum) out.curriculum = acf.curriculum;

    return out;
  }
  return fallback;
}

/**
 * خواندن فهرست نوشته‌ها.
 */
export async function getPosts(fallback) {
  const data = await wpFetch('/wp-json/wp/v2/posts?_embed&per_page=20', null);
  if (Array.isArray(data)) {
    return data.map((p) => ({
      slug: p.slug,
      title: p.title?.rendered || '',
      excerpt: stripHtml(p.excerpt?.rendered) || '',
      body: p.content?.rendered || '',
      date: p.date ? new Date(p.date).toLocaleDateString('fa-IR') : '',
      image: p._embedded?.['wp:featuredmedia']?.[0]?.source_url || null,
    }));
  }
  return fallback;
}

/**
 * خواندن یک نوشته بر اساس اسلاگ.
 */
export async function getPost(slug, fallback) {
  const data = await wpFetch(`/wp-json/wp/v2/posts?slug=${slug}&_embed`, null);
  if (Array.isArray(data) && data.length) {
    const p = data[0];
    return {
      slug: p.slug,
      title: p.title?.rendered || '',
      body: p.content?.rendered || '',
      excerpt: stripHtml(p.excerpt?.rendered) || '',
      date: p.date ? new Date(p.date).toLocaleDateString('fa-IR') : '',
      image: p._embedded?.['wp:featuredmedia']?.[0]?.source_url || null,
    };
  }
  return fallback;
}

/**
 * خواندن محصولات ووکامرس (در صورت فعال بودن).
 */
export async function getProducts(fallback) {
  const key = process.env.NEXT_PUBLIC_WC_CONSUMER_KEY;
  const secret = process.env.NEXT_PUBLIC_WC_CONSUMER_SECRET;
  if (!WP_URL || !key || !secret) return fallback;
  try {
    const res = await fetch(
      `${WP_URL}/wp-json/wc/v3/products?per_page=20&consumer_key=${key}&consumer_secret=${secret}`,
      { next: { revalidate: 60 } }
    );
    if (!res.ok) return fallback;
    const data = await res.json();
    return data.map((p) => ({
      slug: p.slug,
      title: p.name,
      price: p.price_html ? stripHtml(p.price_html) : p.price,
      desc: stripHtml(p.short_description || p.description),
      image: p.images?.[0]?.src || null,
    }));
  } catch {
    return fallback;
  }
}

function stripHtml(html) {
  if (!html) return '';
  return String(html)
    .replace(/<[^>]*>/g, ' ')
    .replace(/\s+/g, ' ')
    .trim();
}

export const isConfigured = Boolean(WP_URL);
