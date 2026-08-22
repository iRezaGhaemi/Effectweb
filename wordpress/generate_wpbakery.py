# -*- coding: utf-8 -*-
"""
تولید محتوای WPBakery (Visual Composer) برای ۹ صفحه سایت «استودیو اثر».

خروجی: wpbakery/*.txt  ← محتوای shortcode هر صفحه (برای paste در WPBakery)

نحوه استفاده:
1. افزونه WPBakery Page Builder را نصب و فعال کنید.
2. صفحه جدید بسازید و ویرایشگر را روی «Backend Editor» (حالت WPBakery) بگذارید.
3. محتوای فایل txt مربوطه را در حالت «Classic Mode» (تب متن) جای‌گذاری کنید.
4. تصاویر را آپلود کنید و شناسه (ID) آن‌ها را در [vc_single_image image="ID"] جایگزین کنید.

اجرا: python3 generate_wpbakery.py
"""
import os

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "wpbakery")
os.makedirs(OUT, exist_ok=True)

# رنگ‌های برند
ROYAL = "#4a00a5"
WHY = "#2d0065"
AMBER = "#ffaa00"
INK = "#16161d"
WHITE = "#ffffff"
BODY = "#3d4350"

# اسلاگ صفحات
SLUG = {
    "home": "https://example.com/",
    "about": "https://example.com/about-us/",
    "academy": "https://example.com/academy/",
    "course": "https://example.com/course/",
    "blog": "https://example.com/blog/",
    "category": "https://example.com/blog-category/",
    "post": "https://example.com/sample-post/",
    "shop": "https://example.com/shop/",
    "product": "https://example.com/pegboard/",
}


def enc(u):
    return u.replace(":", "%3A").replace("/", "%2F").replace("?", "%3F")


def row(content, bg=None, pad_top=60, pad_bottom=60):
    if bg:
        css = ".vc_custom_bg{background-color:%s;padding-top:%dpx;padding-bottom:%dpx;}" % (bg, pad_top, pad_bottom)
        return '[vc_row css="%s"]%s[/vc_row]' % (css, content)
    css = ".vc_custom_pad{padding-top:%dpx;padding-bottom:%dpx;}" % (pad_top, pad_bottom)
    return '[vc_row css="%s"]%s[/vc_row]' % (css, content)


def col(content, width="1/1"):
    return '[vc_column width="%s"]%s[/vc_column]' % (width, content)


def heading(text, tag="h2", color=None, align="right", size=40):
    parts = ["tag:%s" % tag, "text_align:%s" % align, "font_size:%d" % size]
    if color:
        parts.append("color:%s" % color.replace("#", "%23"))
    return '[vc_custom_heading text="%s" font_container="%s" use_theme_fonts="yes"]' % (text, "|".join(parts))


def text(content, align="right"):
    return '[vc_column_text css=".vc_custom_text{text-align:%s;color:%s;}"]%s[/vc_column_text]' % (
        align, BODY, content)


def button(title, url, bg=AMBER, fg=INK, align="right"):
    return '[vc_btn title="%s" style="custom" custom_background="%s" custom_text="%s" shape="round" align="%s" link="url:%s|||"]' % (
        title, bg, fg, align, enc(url))


def spacer(h=40):
    return '[vc_empty_space height="%dpx"]' % h


def image(img_id, align="center"):
    return '[vc_single_image image="%s" img_size="large" alignment="%s"]' % (img_id, align)


def hero(h1, sub, cta_title, cta_url, seed, cta2=None):
    inner = heading(h1, tag="h1", color=WHITE, size=44)
    if sub:
        inner += '[vc_column_text css=".vc_custom_t{text-align:right;color:#ac8ad6;font-size:17px;}"]%s[/vc_column_text]' % sub
    if cta2:
        inner += col(button(cta_title, cta_url, bg=AMBER, fg=INK), "1/2") + col(button(cta2[0], cta2[1], bg=ROYAL, fg=WHITE), "1/2")
    else:
        inner += button(cta_title, cta_url, bg=AMBER, fg=INK)
    return row(col(inner), bg=WHY, pad_top=70, pad_bottom=70)


def services_section():
    items = [
        ("طراحی سایت و اپلیکیشن", "service-web"),
        ("هویت بصری", "service-identity"),
        ("سوشال مدیا", "service-soshial"),
        ("مارکتینگ", "service-marketing"),
        ("سئو", "service-seo"),
        ("تبلیغات", "service-ads"),
    ]
    cols = ""
    for i, (t, _) in enumerate(items):
        cols += col(heading(t, tag="h3", size=18, color=INK), "1/3")
    return row(col(heading("خدمات آژانس دیجیتال اثر", size=36, color=INK))
               + '[vc_column_text css=".vc_custom_t{text-align:right;}"]طراحی سایت و اپلیکیشن، هویت بصری، سوشال مدیا، مارکتینگ، سئو و تبلیغات — راهکارهای اختصاصی برای هر کسب‌وکار.[/vc_column_text]'
               + cols)


# ============ ساخت ۹ صفحه ============
pages = {}

pages["home"] = (
    hero("هم مسیر تا تغییر",
         "خدمات حرفه‌ای تولید محتوا، طراحی سایت، طراحی اپلیکیشن، طراحی لوگو، طراحی هویت برند و طراحی‌های چاپی.",
         "مشاوره رایگان", SLUG["home"] + "#contact", "h1",
         cta2=("مشاهده خدمات", SLUG["home"] + "#services"))
    + services_section()
    + row(col(heading("مفتخر به همکاری با بیش از ۱۰۰ استارتاپ و بیزنس‌های موفق", size=32, color=INK)), bg="#f5f5f5")
    + row(col(heading("چرا اثر را انتخاب کنیم؟", size=32, color=INK)
              + text("تیم تخصصی و حرفه‌ای، تجربه کاربری در اولویت، راهکارهای اختصاصی برای هر کسب‌وکار و ارائه گزارشات روند پروژه.")))
    + row(col(heading("آخرین مقالات و ویدئوها", size=32, color=INK)
              + button("مشاهده بلاگ", SLUG["blog"], bg=ROYAL, fg=WHITE)))
    + row(col(heading("با ما در ارتباط باشید", size=32, color=INK)
              + text("برای شروع همکاری فرم تماس را تکمیل کنید یا با شماره ۰۹۱۵ ۳۸۹ ۲۰۸۸ تماس بگیرید.")
              + button("تماس با ما", SLUG["home"] + "#contact")))
)

pages["about"] = (
    hero("درباره استودیو اثر", "تیم حرفه‌ای و خلاق افکت؛ همراه شما از ایده تا اجرا.", "همکاری با ما", SLUG["home"] + "#contact", "a1")
    + row(col(heading("تیم حرفه‌ای و خلاق افکت", size=32, color=INK)
              + image("ID-TEAM")
              + text("استودیو اثر با تیمی متخصص در طراحی، برنامه‌نویسی و بازاریابی دیجیتال، به کسب‌وکارها کمک می‌کند تا برند خود را بسازند و رشد کنند.")))
    + row(col(heading("مفتخر به همکاری با بیش از ۱۰۰ استارتاپ", size=32, color=INK)), bg="#f5f5f5")
    + row(col(heading("پرسش‌های پرتکرار", size=32, color=INK) + text("پاسخ سوالات متداول درباره خدمات و همکاری با استودیو اثر.")))
)

pages["academy"] = (
    hero("آموزش هدفمند، آینده‌ای روشن", "در دوره‌های آکادمی اثر، اصول و تفکر طراحی را با جدیدترین متدلوژی‌های آموزشی فرا می‌گیرید.", "مشاهده دوره‌ها", SLUG["academy"] + "#courses", "c1")
    + row(col(heading("دسته‌بندی دوره‌ها", size=32, color=INK))
          + col(heading("گرافیک", tag="h3", size=18, color=INK), "1/4")
          + col(heading("برنامه نویسی", tag="h3", size=18, color=INK), "1/4")
          + col(heading("طراحی محصول", tag="h3", size=18, color=INK), "1/4")
          + col(heading("ویدئو و انیمیشن", tag="h3", size=18, color=INK), "1/4"))
    + row(col(heading("دوره جامع Cinema 4D", tag="h3", size=26, color=INK)
              + image("ID-CINEMA4D")
              + text("آموزش جامع نرم‌افزار سینما فوردی برای طراحی سه‌بعدی و موشن گرافیک.")
              + button("مشاهده دوره", SLUG["course"])), bg="#f5f5f5")
    + row(col(heading("دوره جامع فتوشاپ", tag="h3", size=26, color=INK)
              + image("ID-PHOTOSHOP")
              + text("آموزش کامل فتوشاپ از مقدماتی تا پیشرفته برای طراحان.")
              + button("مشاهده دوره", SLUG["course"])))
    + row(col(heading("نظرات مشتریان", size=32, color=INK) + text("دانشجویان و کارفرمایان درباره دوره‌های آکادمی اثر چه می‌گویند.")))
)

pages["blog"] = (
    hero("بلاگ استودیو اثر", "آخرین مقالات، ویدئوها و اخبار دنیای تکنولوژی و طراحی.", "مشاهده مقالات", SLUG["blog"], "b1")
    + row(col(heading("تازه‌های روز", size=32, color=INK))
          + col(heading("رتبه‌بندی تمام ۸ فیلم تاریخی ریدلی اسکات", tag="h3", size=18, color=INK) + button("مطالعه", SLUG["post"], bg=ROYAL, fg=WHITE), "1/3")
          + col(heading("رونمایی از هیوندای الانترا ۲۰۲۷", tag="h3", size=18, color=INK) + button("مطالعه", SLUG["post"], bg=ROYAL, fg=WHITE), "1/3")
          + col(heading("ای‌ام‌دی از انویدیا جلو می‌زند", tag="h3", size=18, color=INK) + button("مطالعه", SLUG["post"], bg=ROYAL, fg=WHITE), "1/3"))
    + row(col(heading("دسته‌بندی‌ها", size=32, color=INK)
              + text("تکنولوژی، نقد و بررسی، خودرو، ویدئو، آموزش، علمی، کسب‌وکار")
              + button("همه دسته‌ها", SLUG["category"], bg="#f5f5f5", fg=INK)))
)

pages["category"] = (
    hero("دسته‌بندی: تکنولوژی", "آخرین مطالب و اخبار حوزه تکنولوژی.", "داغ‌ترین مطالب", SLUG["category"], "k1")
    + row(col(heading("داغ‌ترین مطالب این دسته", size=32, color=INK))
          + col(heading("پیلار کلاستر چیست؟", tag="h4", size=17, color=INK) + button("مطالعه", SLUG["post"], bg=ROYAL, fg=WHITE), "1/3")
          + col(heading("رونمایی از هیوندای الانترا ۲۰۲۷", tag="h4", size=17, color=INK) + button("مطالعه", SLUG["post"], bg=ROYAL, fg=WHITE), "1/3")
          + col(heading("فاز جدید جنگ فناوری", tag="h4", size=17, color=INK) + button("مطالعه", SLUG["post"], bg=ROYAL, fg=WHITE), "1/3"))
)

pages["post"] = (
    hero("رونمایی از هیوندای الانترا ۲۰۲۷", "تغییرات گسترده در نسل جدید هیوندای الانترا.", "بازگشت به بلاگ", SLUG["blog"], "t1")
    + row(col(heading("تغییرات گسترده در نسل جدید هیوندای الانترا", size=28, color=INK)
              + text("هیوندای الانترا ۲۰۲۷ با طراحی جدید، ابعاد بزرگ‌تر و امکانات فناورانه‌تر معرفی شد.")))
    + row(col(heading("هیوندای الانترا جدید عضلانی‌تر می‌شود", size=28, color=INK)
              + text("در این نسل، فرم بدنه اسپرت‌تر شده و از پیشرانه‌های بهینه‌تر بهره می‌برد.")))
    + row(col(heading("تازه‌های تکنولوژی", size=24, color=INK)
              + text("پیلار کلاستر چیست؟ استراتژی هوشمندانه برای افزایش ترافیک و بهبود سئو")
              + button("مطالعه بیشتر", SLUG["blog"], bg=ROYAL, fg=WHITE)), bg="#f5f5f5")
)

pages["shop"] = (
    hero("محصولات با تخفیف استثنایی", "دوره‌های آموزشی، محصولات دیجیتال و پکیج‌های استودیو اثر.", "مشاهده محصولات", SLUG["shop"] + "#products", "s1")
    + row(col(heading("محصولات", size=32, color=INK))
          + col(heading("پگ بورد رو میزی", tag="h3", size=18, color=INK) + image("ID-PRODUCT") + text("قیمت: ۲,۴۹۸,۰۰۰ تومان") + button("مشاهده", SLUG["product"]), "1/3")
          + col(heading("پگ بورد رو میزی", tag="h3", size=18, color=INK) + image("ID-PRODUCT") + text("قیمت: ۲,۴۹۸,۰۰۰ تومان") + button("مشاهده", SLUG["product"]), "1/3")
          + col(heading("پگ بورد رو میزی", tag="h3", size=18, color=INK) + image("ID-PRODUCT") + text("قیمت: ۲,۴۹۸,۰۰۰ تومان") + button("مشاهده", SLUG["product"]), "1/3"))
    + row(col(heading("پرسش‌های پرتکرار", size=32, color=INK) + text("سوالات متداول درباره خرید و ارسال سفارش.")))
)

pages["product"] = (
    hero("پگ بورد رو میزی", "ابزار منظم‌سازی میز کار با طراحی مدرن.", "افزودن به سبد", SLUG["product"], "r1")
    + row(col(heading("توضیحات محصول", size=32, color=INK)
              + image("ID-PRODUCT")
              + text("پگ بورد رو میزی استودیو اثر برای سازمان‌دهی ابزار و لوازم روی میز کار طراحی شده است.")
              + '[vc_column_text css=".vc_custom_t{text-align:right;color:#4a00a5;font-size:18px;font-weight:700;}"]قیمت: ۲,۴۹۸,۰۰۰ تومان[/vc_column_text]'))
    + row(col(heading("محصولات مرتبط", size=28, color=INK)
              + col(heading("پگ بورد رو میزی", tag="h3", size=18, color=INK) + button("مشاهده", SLUG["product"]), "1/3")
              + col(heading("پگ بورد رو میزی", tag="h3", size=18, color=INK) + button("مشاهده", SLUG["product"]), "1/3")
              + col(heading("پگ بورد رو میزی", tag="h3", size=18, color=INK) + button("مشاهده", SLUG["product"]), "1/3")), bg="#f5f5f5")
)

pages["course"] = (
    hero("دوره جامع فتوشاپ", "آموزش کامل فتوشاپ از مقدماتی تا پیشرفته.", "ثبت‌نام در دوره", SLUG["course"] + "#curriculum", "d1")
    + row(col(heading("توضیحات دوره", size=32, color=INK)
              + image("ID-PHOTOSHOP-INTRO")
              + text("در این دوره، اصول و تکنیک‌های طراحی گرافیک در فتوشاپ را از پایه یاد می‌گیرید.")))
    + row(col(heading("آنچه در دوره آموزش جامع فتوشاپ خواهید دید:", size=28, color=INK)
              + text("مبانی فتوشاپ، روتوش تصویر، طراحی پوستر، کار با لایه‌ها و ماسک، خروجی حرفه‌ای.")), bg="#f5f5f5")
    + row(col(heading("گواهینامه پایان دوره آکادمی اثر", size=28, color=INK)
              + image("ID-CERTIFICATE")
              + text("پس از پایان دوره، گواهینامه معتبر آکادمی اثر دریافت می‌کنید.")))
    + row(col(heading("دوره‌های مرتبط", size=32, color=INK)
              + col(heading("دوره جامع Cinema 4D", tag="h3", size=18, color=INK) + button("مشاهده", SLUG["course"]), "1/3")
              + col(heading("دوره جامع Cinema 4D", tag="h3", size=18, color=INK) + button("مشاهده", SLUG["course"]), "1/3")
              + col(heading("دوره جامع Cinema 4D", tag="h3", size=18, color=INK) + button("مشاهده", SLUG["course"]), "1/3")))
)

# ---------- خروجی ----------
filenames = {
    "home": "home", "about": "about-us", "academy": "academy",
    "blog": "blog", "category": "category", "post": "post",
    "shop": "shop", "product": "product", "course": "course",
}

header_note = """<!-- ============================================================
صفحه: %s
قالب: WPBakery (Visual Composer)
نحوه استفاده:
1) صفحه جدید بسازید و ویرایشگر را روی Backend Editor بگذارید.
2) این محتوا را در تب «متن/کلاسیک» جای‌گذاری کنید.
3) شناسه تصاویر (ID-xxx) را بعد از آپلود تصاویر در Media جایگزین کنید.
4) لینک‌ها را (example.com) با دامنه واقعی خودتان عوض کنید.
============================================================ -->
"""

combined = []
for key, name in filenames.items():
    content = header_note % name + pages[key]
    fn = os.path.join(OUT, "%s.txt" % name)
    with open(fn, "w", encoding="utf-8") as fh:
        fh.write(content)
    combined.append(content)
    print("wrote", fn)

all_fn = os.path.join(OUT, "all-pages.txt")
with open(all_fn, "w", encoding="utf-8") as fh:
    fh.write("\n\n".join(combined))
print("wrote", all_fn)
print("DONE: 9 pages + combined")
