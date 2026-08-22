# افزونه‌ها (Plugins) — پکیج استودیو اثر

## 📦 ACF (Advanced Custom Fields) — نسخه 6.8.8

پلاگین رایگان ACF برای ساخت فیلدهای سفارشی که در معماری headless استفاده می‌شود.

### فایل‌ها

```
plugins/
├── advanced-custom-fields/        ← پوشه کامل پلاگین (برای آپلود دستی با FTP)
├── advanced-custom-fields.zip     ← بسته قابل نصب (Plugins → Add New → Upload)
├── acf-field-groups.json          ← گروه‌های فیلد سفارشی (قابل ایمپورت)
└── generate_acf_fields.py         ← اسکریپت تولید گروه‌های فیلد
```

### نصب

1. فایل `advanced-custom-fields.zip` را از **Plugins → Add New → Upload Plugin** آپلود کنید.
   - ⚠️ اگر به دلیل حجم (۴.۵MB بالاتر از حد پیش‌فرض ۲MB) خطا داد، پوشه
     `advanced-custom-fields/` را با FTP/File Manager در `wp-content/plugins/` آپلود کنید.
2. افزونه **Advanced Custom Fields** را فعال کنید.

### ایمپورت گروه‌های فیلد سفارشی

1. مسیر: **Custom Fields → Tools → Import Field Groups**
2. فایل `acf-field-groups.json` را آپلود کنید.

این کار ۴ گروه فیلد می‌سازد که دقیقاً با فرانت‌اند headless هماهنگ هستند:

| گروه فیلد | نمایش در | فیلدها |
|---|---|---|
| صفحه اصلی | صفحه نخست (front page) | hero_title، hero_subtitle، services، stats، why |
| درباره ما | برگه «درباره ما» | hero_text، body |
| آکادمی | برگه «آکادمی» | hero_text، body، courses |
| دوره | برگه «دوره» | hero_text، body، curriculum |

> ⚠️ **نکته مهم:** گروه‌های «درباره ما»، «آکادمی» و «دوره» به‌صورت پیش‌فرض روی
> «همه برگه‌ها» تنظیم شده‌اند. برای دقت بیشتر، بعد از ایمپورت، در تنظیمات هر
> گروه فیلد (Location) به‌جای «برگه»، برگه مشخص (مثلاً «درباره ما») را انتخاب کنید.

### نحوه اتصال به REST API

در تنظیمات هر گروه فیلد، گزینه **«Show in REST API»** فعال است (در JSON هم
`show_in_rest: 1` تنظیم شده). با این کار فیلدها زیر کلید `acf` در پاسخ REST
قرار می‌گیرند و فرانت‌اند headless آن‌ها را می‌خواند.

---

## منبع دانلود

- مخزن رسمی ACF (رایگان، GPL): https://github.com/AdvancedCustomFields/acf
- نسخه دانلودشده: 6.8.8
- (به دلیل محدودیت شبکه این محیط، از مخزن رسمی GitHub دانلود شد؛ نه wordpress.org)
