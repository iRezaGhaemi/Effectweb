# فونت وزیرمتن (Vazirmatn)

این پوشه برای نگهداری محلی فونت وزیرمتن در نظر گرفته شده است.

قالب به‌صورت پیش‌فرض فونت را از Google Fonts بارگذاری می‌کند. برای بارگذاری محلی (پیشنهادی برای سرعت و سازگاری با ایران):

1. فایل‌های فونت را از این‌جا دانلود کنید:
   https://github.com/rastikerdar/vazirmatn/releases

2. فایل‌های `woff2` را در همین پوشه (`assets/fonts/`) قرار دهید.

3. در `functions.php`، فیلتر `effect_studio_font_url` را به یک `@font-face` محلی تغییر دهید
   (یا فونت را از طریق افزونه‌های فونت فارسی مدیریت کنید).

مثال `@font-face`:

```css
@font-face {
  font-family: "Vazirmatn";
  src: url("fonts/Vazirmatn-Regular.woff2") format("woff2");
  font-weight: 400;
  font-display: swap;
}
```
