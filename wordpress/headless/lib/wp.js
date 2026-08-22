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
 * فیلدهای ACF (در صورت وجود) روی آبجکت acf برگردانده می‌شوند.
 */
export async function getPage(slug, fallback) {
  const data = await wpFetch(
    `/wp-json/wp/v2/pages?slug=${slug}&_embed`,
    null
  );
  if (Array.isArray(data) && data.length) {
    const p = data[0];
    return {
      title: p.title?.rendered || fallback?.title,
      hero: p.acf?.hero || fallback?.hero,
      body: p.acf?.body || stripHtml(p.content?.rendered) || fallback?.body,
      acf: p.acf || {},
    };
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
