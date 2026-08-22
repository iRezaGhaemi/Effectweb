# پوشه frozen/ — صفحات پیکسل‌پرفکت

این پوشه محل نگهداری فایل‌های HTML اصلی سایت است تا قالب «پیکسل‌پرفکت» (`template-frozen.php`) بتواند آن‌ها را به‌صورت خام سرو کند.

## چرا این پوشه خالی است؟

فایل‌های HTML اصلی حدود ۳۲ مگابایت حجم دارند (به دلیل تصاویر base64 داخل آن‌ها). برای اینکه فایل ZIP قالب سبک بماند و از حد مجاز آپلود وردپرس (۲ مگابایت) عبور نکند، این فایل‌ها جدا از قالب قرار می‌گیرند.

## چگونه فایل‌ها را اضافه کنید؟

1. از پوشه `pixel-perfect/` در مخزن (یا از فایل‌هایی که در اختیار دارید)، این ۹ فایل را بردارید:
   - `effect-studio.html`
   - `effect-studio-about-us.html`
   - `effect-studio-academy.html`
   - `effect-studio-course.html`
   - `effect-studio-blog.html`
   - `effect-studio-category.html`
   - `effect-studio-post.html`
   - `effect-studio-shop.html`
   - `effect-studio-product.html`

2. آن‌ها را در همین پوشه (`wp-content/themes/effect-studio/frozen/`) آپلود کنید (با FTP یا File Manager).

3. برای هر صفحه، قالب «پیکسل‌پرفکت (فایل HTML اصلی)» را انتخاب کنید:
   - در ویرایشگر برگه، از بخش «قالب» (Template) در ستون کناری، این قالب را انتخاب کنید.

## نقشه اسلاگ → فایل

| اسلاگ صفحه | فایل HTML |
|---|---|
| home | effect-studio.html |
| about-us | effect-studio-about-us.html |
| academy | effect-studio-academy.html |
| course | effect-studio-course.html |
| blog | effect-studio-blog.html |
| blog-category | effect-studio-category.html |
| sample-post | effect-studio-post.html |
| shop | effect-studio-shop.html |
| pegboard | effect-studio-product.html |

> 💡 اگر فقط پیکسل‌پرفکت می‌خواهید و نیازی به وردپرس ندارید، ساده‌ترین راه این است که فایل‌های پوشه `pixel-perfect/` را مستقیم در ریشه هاست آپلود کنید (بدون وردپرس).
