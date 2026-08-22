# فونت وزیرمتن (Vazirmatn)

فونت وزیرمتن به‌صورت **محلی** در این پوشه قرار دارد و قالب آن را بدون نیاز به Google Fonts بارگذاری می‌کند.

## فایل‌ها

- `Vazirmatn-Variable.woff2` — فونت متغیر (وزن‌های ۱۰۰ تا ۹۰۰ در یک فایل)
- `Vazirmatn-Regular.woff2` — وزن عادی (۴۰۰)
- `Vazirmatn-Bold.woff2` — وزن ضخیم (۷۰۰)

## لایسنس

فونت وزیرمتن تحت مجوز [OFL-1.1 (SIL Open Font License)](https://openfontlicense.org) منتشر شده است.

منبع: https://github.com/rastikerdar/vazirmatn

## تعریف @font-face

تعریف فونت در فایل `style.css` قالب انجام شده است:

```css
@font-face {
  font-family: "Vazirmatn";
  src: url("fonts/Vazirmatn-Variable.woff2") format("woff2-variations");
  font-weight: 100 900;
  font-display: swap;
}
```

> نکته: اگر فونت‌های بیشتری می‌خواهید، آن‌ها را از مخزن رسمی
> https://github.com/rastikerdar/vazirmatn/releases دانلود کنید.

