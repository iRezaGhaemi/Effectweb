# استودیو اثر — پکیج نهایی و قابل استفاده

این مخزن شامل **بازسازی کامل سایت «استودیو اثر»** در چند روش استقرار است. بسته به نیازتان یکی را انتخاب کنید.

---

## 📋 روش‌های استقرار (چکیده)

| # | روش | پکیج | ویرایش محتوا | ظاهر | نیازمندی |
|---|---|---|---|---|---|
| ۱ | **Headless وردپرس** ⭐ | `effect-studio-headless.zip` | ✅ خیلی راحت (پیشخوان) | ✅ خیلی نزدیک | وردپرس + Node |
| ۲ | وردپرس + المنتور | `wordpress/effect-studio.zip` | ✅ راحت | نزدیک | وردپرس + المنتور |
| ۳ | وردپرس + WPBakery | `wordpress/wpbakery/*.txt` | ✅ راحت | نزدیک | وردپرس + WPBakery |
| ۴ | پیکسل‌پرفکت (استاتیک) | `effect-studio-pixel-perfect.zip` | ❌ دستی (کد) | ✅ ۱۰۰٪ | فقط هاست ساده |

> ⭐ **توصیه:** روش ۱ (Headless) بهترین تعادل بین «ویرایش راحت» و «ظاهر دقیق» است.

---

## ⭐ روش ۱ — Headless وردپرس (توصیه‌شده)

معماری: وردپرس به‌عنوان backend (مدیریت محتوا) + فرانت‌اند Next.js که از REST API می‌خواند.

```
وردپرس (پیشخوان)  ──REST API──►  Next.js (فرانت‌اند)
   ویرایش محتوا                    نمایش + انیمیشن‌ها
```

### ساختار پکیج

```
effect-studio-headless.zip
├── headless/                ← فرانت‌اند Next.js (کد منبع)
│   ├── pages/               ← ۹ صفحه
│   ├── components/          ← هدر، فوتر، انیمیشن‌ها
│   ├── lib/wp.js            ← اتصال به REST API
│   ├── lib/content.js       ← محتوای fallback
│   ├── styles/tailwind.css  ← CSS واقعی سایت (همه انیمیشن‌ها)
│   ├── public/fonts/        ← فونت وزیرمتن (محلی)
│   ├── public/images/       ← تصاویر واقعی
│   └── .env.example         ← تنظیمات اتصال به وردپرس
├── wordpress/               ← بخش وردپرس (backend)
│   ├── effect-studio.zip    ← قالب قابل نصب
│   ├── advanced-custom-fields.zip ← پلاگین ACF
│   ├── effect-studio-api/   ← پلاگین API اختصاصی
│   └── acf-field-groups.json ← فیلدهای ACF
└── README.md                ← همین راهنما
```

### 🚀 نصب (گام‌به‌گام)

**الف) سمت وردپرس (backend):**

1. وردپرس را نصب و زبان را «فارسی» کنید.
2. پلاگین `advanced-custom-fields.zip` را نصب و فعال کنید.
3. پوشه `effect-studio-api/` را در `wp-content/plugins/` بگذارید و فعال کنید.
4. فایل `acf-field-groups.json` را از **Custom Fields → Tools → Import** وارد کنید.
5. محتوا را در برگه‌ها/نوشته‌ها تایپ کنید.

اندپوینت‌های API آماده:
- `/wp-json/effect/v1/global` — برند، منو، تماس
- `/wp-json/effect/v1/home` — صفحه اصلی
- `/wp-json/effect/v1/section/about-us` و `/academy` و `/course`
- `/wp-json/effect/v1/posts` و `/posts/{slug}`
- `/wp-json/effect/v1/products`

**ب) سمت فرانت‌اند (Next.js):**

```bash
cd headless
npm install
cp .env.example .env.local   # و آدرس وردپرس را بنویسید
npm run build
npm run start
```

در `.env.local`:
```
NEXT_PUBLIC_WP_URL=https://your-domain.com
```

> بدون وردپرس هم کار می‌کند (از محتوای fallback استفاده می‌کند) — برای پیش‌نمایش.

**استقرار:** روی Vercel، Netlify یا هر سرور Node (`npm run build && npm start`).

---

## 📦 سایر پکیج‌ها

### `wordpress/effect-studio.zip` — قالب وردپرس + المنتور
قالب کامل (هدر/فوتر اختصاصی، RTL، فونت محلی، ووکامرس، نصب خودکار ۹ صفحه). نصب: **Appearance → Themes → Upload**.

### `wordpress/wpbakery/` — WPBakery (Visual Composer)
فایل‌های shortcode هر ۹ صفحه. جای‌گذاری در Backend Editor.

### `effect-studio-pixel-perfect.zip` — نسخه استاتیک
فایل‌های HTML اصلی. آپلود در ریشه هاست = سایت ۱۰۰٪ یکسان (اما بدون ویرایش راحت).

---

## 📄 مستندات

- `Effect-Studio-Setup-Guide.pdf` — راهنمای راه‌اندازی (فارسی، ۷ صفحه)
- `Effect-Studio-Test-Checklist.pdf` — چک‌لیست تست (فارسی، ۴ صفحه)
- `wordpress/README-fa.md` — راهنمای تفصیلی وردپرس
- `wordpress/headless/README-fa.md` — راهنمای تفصیلی headless

---

## 🎨 مشخصات برند

- **رنگ اصلی:** `#4a00a5` (بنفش) | **تیره:** `#2d0065` | **CTA:** `#ffaa00` (کهربایی)
- **فونت:** وزیرمتن (Vazirmatn) — محلی، بدون نیاز به Google Fonts
- **راست‌چین:** RTL کامل

## 🎬 انیمیشن‌های پیاده‌شده (در headless)

- `animate-marquee` (40s) — اسلایدر لوگوی مشتریان + `animate-twinkle`
- `animate-why-up` / `why-down` — ستون‌های متحرک «چرا اثر»
- `animate-pf-scroll` (30s) — اسکرول نمونه‌کارها (توقف با hover)
- `animate-marquee-slow` (20s) — نظرات مشتریان
