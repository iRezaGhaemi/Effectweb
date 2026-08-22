# -*- coding: utf-8 -*-
"""
تولید خروجی‌های وردپرس + المنتور برای سایت «استودیو اثر»

خروجی‌ها:
1. elementor-templates/*.json   ← قالب‌های المنتور (فقط بدنه، بدون هدر/فوتر) برای ایمپورت دستی
2. theme/effect-studio/inc/pages/*.json  ← همان بدنه‌ها + متادیتای صفحات (برای نصب خودکار)
3. effect-studio.zip            ← بسته قابل نصب قالب (از پوشه theme/effect-studio)

اجرا: python3 generate_templates.py
"""
import json, hashlib, os, zipfile, re, base64

BASE = os.path.dirname(os.path.abspath(__file__))

# ---------- برند ----------
C = {
    "royal": "#4a00a5", "royal2": "#5e01a4", "violet": "#6e33b7",
    "lilac": "#ac8ad6", "why": "#2d0065", "amber": "#FFAA00",
    "amberDark": "#e89b00", "ink": "#16161d", "body": "#3d4350",
    "panel": "#fafafa", "mist": "#f5f5f5", "line": "#e0e2e7", "white": "#ffffff",
}

# اسلاگ صفحات وردپرس (لینک‌های داخلی)
SLUG = {
    "home": "/", "about": "/about-us/", "academy": "/academy/",
    "course": "/course/", "blog": "/blog/", "category": "/blog-category/",
    "post": "/sample-post/", "shop": "/shop/", "product": "/pegboard/",
}

# ---------- متادیتای صفحات ----------
PAGES = [
    dict(key="home",     slug="home",         title="صفحه اصلی",     menu="استودیو اثر",  front_page=True),
    dict(key="about-us", slug="about-us",     title="درباره ما",     menu="درباره ما"),
    dict(key="academy",  slug="academy",      title="آکادمی",        menu="آکادمی"),
    dict(key="course",   slug="course",       title="دوره جامع فتوشاپ", menu="دوره ها"),
    dict(key="blog",     slug="blog",         title="بلاگ",          menu="بلاگ",         posts_page=True),
    dict(key="category", slug="blog-category", title="دسته‌بندی: تکنولوژی"),
    dict(key="post",     slug="sample-post",  title="نمونه نوشته"),
    dict(key="shop",     slug="shop",         title="فروشگاه",       menu="فروشگاه"),
    dict(key="product",  slug="pegboard",     title="پگ بورد رو میزی"),
]

# ---------- ابزار ساخت المنت ----------
def uid(seed):
    return hashlib.md5(seed.encode("utf-8")).hexdigest()[:8]

def w(widgetType, settings, seed):
    return {"id": uid(seed), "elType": "widget", "widgetType": widgetType,
            "isInner": False, "settings": settings, "elements": []}

def box(settings, elements, seed):
    return {"id": uid(seed), "elType": "container", "isInner": False,
            "settings": settings, "elements": elements}

def pad(v):
    return {"unit": "px", "top": str(v), "right": str(v), "bottom": str(v), "left": str(v), "isLinked": True}

def radius(v):
    return {"unit": "px", "top": str(v), "right": str(v), "bottom": str(v), "left": str(v), "isLinked": True}

def heading(title, seed, size=40, color=None, align="right", weight="700", tag="h2", line=1.3):
    s = {"title": title, "header_size": tag, "align": align,
         "typography_typography": "custom",
         "typography_font_size": {"unit": "px", "size": size, "sizes": []},
         "typography_font_weight": weight,
         "typography_line_height": {"unit": "em", "size": line, "sizes": []}}
    if color:
        s["title_color"] = color
    return w("heading", s, seed)

def text(html, seed, color=C["body"], align="right", size=16, line=1.8, weight="400"):
    return w("text-editor", {"editor": html, "align": align, "text_color": color,
                             "typography_typography": "custom",
                             "typography_font_size": {"unit": "px", "size": size, "sizes": []},
                             "typography_font_weight": weight,
                             "typography_line_height": {"unit": "em", "size": line, "sizes": []}}, seed)

def button(text_, url, seed, bg=C["amber"], color=C["ink"], size=16, rd=12, weight="600", align="right"):
    return w("button", {"text": text_, "align": align,
                        "link": {"url": url, "is_external": "", "nofollow": "", "custom_attributes": ""},
                        "background_color": bg, "button_text_color": color,
                        "border_radius": radius(rd),
                        "typography_typography": "custom",
                        "typography_font_size": {"unit": "px", "size": size, "sizes": []},
                        "typography_font_weight": weight}, seed)

def spacer(h, seed):
    return w("spacer", {"space": {"unit": "px", "size": h, "sizes": []}}, seed)

# ---------- تصاویر واقعی (استخراج‌شده از فایل‌های HTML اصلی) ----------
IMG_DIR = os.path.join(BASE, "assets", "images")
_IMG_CACHE = {}


def _img_uri(name):
    """خواندن تصویر و برگرداندن data URI (با کش)."""
    if name in _IMG_CACHE:
        return _IMG_CACHE[name]
    for ext in ("png", "webp", "jpeg", "jpg"):
        p = os.path.join(IMG_DIR, "%s.%s" % (name, ext))
        if os.path.exists(p):
            data = base64.b64encode(open(p, "rb").read()).decode("ascii")
            mime = {"png": "image/png", "webp": "image/webp", "jpeg": "image/jpeg", "jpg": "image/jpeg"}[ext]
            uri = "data:%s;base64,%s" % (mime, data)
            _IMG_CACHE[name] = uri
            return uri
    return None


def image(name, seed, alt="", align="center", max_w=None, radius_px=0):
    """ویجت تصویر با data URI (برای نمایش بدون نیاز به آپلود جداگانه)."""
    uri = _img_uri(name)
    if not uri:
        return spacer(0, seed)
    s = {"image": {"url": uri, "id": "", "size": "full", "alt": alt}, "align": align}
    if max_w:
        s["width"] = {"unit": "px", "size": max_w, "sizes": []}
    if radius_px:
        s["image_border_radius"] = radius(radius_px)
    return w("image", s, seed)

def section(bg=None, elements=None, seed="s", pt=60, pb=60, px=20, gap=20):
    s = {"padding": {"unit": "px", "top": str(pt), "right": str(px), "bottom": str(pb),
                     "left": str(px), "isLinked": False}, "gap": {"unit": "px", "size": gap, "sizes": []}}
    if bg:
        s["background_background"] = "classic"
        s["background_color"] = bg
    return box(s, elements or [], seed)

def row(cols, seed, gap=20, valign="center"):
    els = []
    for i, (e, width) in enumerate(cols):
        els.append(box({"width": {"unit": "%", "size": width, "sizes": []},
                        "flex_direction": "column", "align_items": "stretch"},
                       e, seed + "-c%d" % i))
    return box({"flex_direction": "row", "gap": {"unit": "px", "size": gap, "sizes": []},
                "align_items": valign}, els, seed)

def hero(h1, sub, cta_text, cta_url, seed, cta2=None, bg=C["why"]):
    items = [heading(h1, seed + "-h1", size=44, color=C["white"], tag="h1", weight="800")]
    if sub:
        items.append(text(sub, seed + "-sub", color=C["lilac"], size=17))
    if cta2:
        items.append(row([([button(cta_text, cta_url, seed + "-b1", bg=C["amber"], color=C["ink"])], 50),
                          ([button(cta2[0], cta2[1], seed + "-b2", bg=C["royal"], color=C["white"])], 50)],
                         seed + "-btns", gap=12))
    else:
        items.append(button(cta_text, cta_url, seed + "-b1", bg=C["amber"], color=C["ink"]))
    return section(bg=bg, elements=items, seed=seed, pt=70, pb=70)

# ======================================================================
# بدنه صفحات (بدون هدر/فوتر)
# ======================================================================
BODIES = {}

BODIES["home"] = [
    hero("هم مسیر تا تغییر",
         "خدمات حرفه‌ای تولید محتوا، طراحی سایت، طراحی اپلیکیشن، طراحی لوگو، طراحی هویت برند و طراحی‌های چاپی.",
         "مشاوره رایگان", SLUG["home"] + "#contact", "p1",
         cta2=("مشاهده خدمات", SLUG["home"] + "#services")),
    section(seed="p2", elements=[
        heading("خدمات آژانس دیجیتال اثر", "p2-h", color=C["ink"]),
        text("طراحی سایت و اپلیکیشن، هویت بصری، سوشال مدیا، مارکتینگ، سئو و تبلیغات — راهکارهای اختصاصی برای هر کسب‌وکار.", "p2-t"),
        image("service-identity", "p2-img", alt="هویت بصری", max_w=360, radius_px=16),
        row([([heading("طراحی سایت و اپلیکیشن", "p2-1", size=18, color=C["ink"], tag="h3")], 33),
             ([heading("هویت بصری", "p2-2", size=18, color=C["ink"], tag="h3")], 33),
             ([heading("سوشال مدیا", "p2-3", size=18, color=C["ink"], tag="h3")], 33)], "p2-r1"),
        row([([heading("مارکتینگ", "p2-4", size=18, color=C["ink"], tag="h3")], 33),
             ([heading("سئو", "p2-5", size=18, color=C["ink"], tag="h3")], 33),
             ([heading("تبلیغات", "p2-6", size=18, color=C["ink"], tag="h3")], 33)], "p2-r2"),
    ]),
    section(bg=C["mist"], seed="p3", elements=[
        heading("مفتخر به همکاری با بیش از ۱۰۰ استارتاپ و بیزنس‌های موفق", "p3-h", color=C["ink"], size=32),
    ]),
    section(seed="p4", elements=[
        heading("چرا اثر را انتخاب کنیم؟", "p4-h", color=C["ink"]),
        text("تیم تخصصی و حرفه‌ای، تجربه کاربری در اولویت، راهکارهای اختصاصی برای هر کسب‌وکار و ارائه گزارشات روند پروژه.", "p4-t"),
    ]),
    section(seed="p5", elements=[
        heading("آخرین مقالات و ویدئوها", "p5-h", color=C["ink"]),
        button("مشاهده بلاگ", SLUG["blog"], "p5-b", bg=C["royal"], color=C["white"]),
    ]),
    section(seed="p6", elements=[
        heading("با ما در ارتباط باشید", "p6-h", color=C["ink"]),
        text("برای شروع همکاری فرم تماس را تکمیل کنید یا با شماره ۰۹۱۵ ۳۸۹ ۲۰۸۸ تماس بگیرید.", "p6-t"),
        button("تماس با ما", SLUG["home"] + "#contact", "p6-b", bg=C["amber"], color=C["ink"]),
    ]),
]

BODIES["about-us"] = [
    hero("درباره استودیو اثر", "تیم حرفه‌ای و خلاق افکت؛ همراه شما از ایده تا اجرا.", "همکاری با ما", SLUG["home"] + "#contact", "a1"),
    section(seed="a2", elements=[
        heading("تیم حرفه‌ای و خلاق افکت", "a2-h", color=C["ink"]),
        text("استودیو اثر با تیمی متخصص در طراحی، برنامه‌نویسی و بازاریابی دیجیتال، به کسب‌وکارها کمک می‌کند تا برند خود را بسازند و رشد کنند.", "a2-t"),
        image("team-reza", "a2-img", alt="رضا قائمی", max_w=320, radius_px=16),
    ]),
    section(bg=C["mist"], seed="a3", elements=[
        heading("مفتخر به همکاری با بیش از ۱۰۰ استارتاپ و بیزنس‌های موفق", "a3-h", color=C["ink"], size=32),
        image("about-map", "a3-img", alt="موقعیت استودیو اثر روی نقشه", max_w=640, radius_px=16),
    ]),
    section(seed="a4", elements=[
        heading("پرسش‌های پرتکرار", "a4-h", color=C["ink"]),
        text("پاسخ سوالات متداول درباره خدمات و همکاری با استودیو اثر.", "a4-t"),
    ]),
]

BODIES["academy"] = [
    hero("آموزش هدفمند، آینده‌ای روشن", "در دوره‌های آکادمی اثر، اصول و تفکر طراحی را با جدیدترین متدلوژی‌های آموزشی فرا می‌گیرید.",
         "مشاهده دوره‌ها", SLUG["academy"] + "#courses", "c1"),
    section(seed="c2", elements=[
        heading("دسته‌بندی دوره‌ها", "c2-h", color=C["ink"]),
        row([([heading("گرافیک", "c2-1", size=18, color=C["ink"], tag="h3")], 25),
             ([heading("برنامه نویسی", "c2-2", size=18, color=C["ink"], tag="h3")], 25),
             ([heading("طراحی محصول", "c2-3", size=18, color=C["ink"], tag="h3")], 25),
             ([heading("ویدئو و انیمیشن", "c2-4", size=18, color=C["ink"], tag="h3")], 25)], "c2-r"),
    ]),
    section(bg=C["mist"], seed="c3", elements=[
        heading("دوره جامع Cinema 4D", "c3-h", color=C["ink"], size=26, tag="h3"),
        image("course-cinema4d", "c3-img", alt="دوره جامع Cinema 4D", max_w=420, radius_px=16),
        text("آموزش جامع نرم‌افزار سینما فوردی برای طراحی سه‌بعدی و موشن گرافیک.", "c3-t"),
        button("مشاهده دوره", SLUG["course"], "c3-b", bg=C["amber"], color=C["ink"]),
    ]),
    section(seed="c4", elements=[
        heading("دوره جامع فتوشاپ", "c4-h", color=C["ink"], size=26, tag="h3"),
        image("course-photoshop", "c4-img", alt="دوره جامع فتوشاپ", max_w=420, radius_px=16),
        text("آموزش کامل فتوشاپ از مقدماتی تا پیشرفته برای طراحان.", "c4-t"),
        button("مشاهده دوره", SLUG["course"], "c4-b", bg=C["amber"], color=C["ink"]),
    ]),
    section(seed="c5", elements=[
        heading("نظرات مشتریان", "c5-h", color=C["ink"]),
        text("دانشجویان و کارفرمایان درباره دوره‌های آکادمی اثر چه می‌گویند.", "c5-t"),
    ]),
]

BODIES["blog"] = [
    hero("بلاگ استودیو اثر", "آخرین مقالات، ویدئوها و اخبار دنیای تکنولوژی و طراحی.", "مشاهده مقالات", SLUG["blog"], "b1"),
    section(seed="b2", elements=[
        heading("تازه‌های روز", "b2-h", color=C["ink"]),
        row([([heading("رتبه‌بندی تمام ۸ فیلم تاریخی ساخته ریدلی اسکات؛ از Robin Hood تا Gladiator II", "b2-1", size=18, color=C["ink"], tag="h3"), button("مطالعه", SLUG["post"], "b2-1b", bg=C["royal"], color=C["white"])], 33),
             ([heading("رونمایی از هیوندای الانترا ۲۰۲۷؛ بزرگ‌تر، لوکس‌تر و مجهز به فناوری‌های نوین", "b2-2", size=18, color=C["ink"], tag="h3"), button("مطالعه", SLUG["post"], "b2-2b", bg=C["royal"], color=C["white"])], 33),
             ([heading("ای‌ام‌دی از انویدیا جلو می‌زند؛ پیش‌بینی فروش بالاتر EPYC Venice", "b2-3", size=18, color=C["ink"], tag="h3"), button("مطالعه", SLUG["post"], "b2-3b", bg=C["royal"], color=C["white"])], 33)], "b2-r"),
    ]),
    section(seed="b3", elements=[
        heading("دسته‌بندی‌ها", "b3-h", color=C["ink"]),
        text("تکنولوژی، نقد و بررسی، خودرو، ویدئو، آموزش، علمی، کسب‌وکار", "b3-t"),
        button("همه دسته‌ها", SLUG["category"], "b3-b", bg=C["mist"], color=C["ink"]),
    ]),
]

BODIES["category"] = [
    hero("دسته‌بندی: تکنولوژی", "آخرین مطالب و اخبار حوزه تکنولوژی.", "داغ‌ترین مطالب", SLUG["category"], "k1"),
    section(seed="k2", elements=[
        heading("داغ‌ترین مطالب این دسته", "k2-h", color=C["ink"]),
        row([([heading("پیلار کلاستر چیست؟ استراتژی هوشمندانه برای افزایش ترافیک و بهبود سئو", "k2-1", size=17, color=C["ink"], tag="h4"), button("مطالعه", SLUG["post"], "k2-1b", bg=C["royal"], color=C["white"])], 33),
             ([heading("رونمایی از هیوندای الانترا ۲۰۲۷", "k2-2", size=17, color=C["ink"], tag="h4"), button("مطالعه", SLUG["post"], "k2-2b", bg=C["royal"], color=C["white"])], 33),
             ([heading("فاز جدید جنگ فناوری: آمریکا ممنوعیت‌های واردات تجهیزات چینی را افزایش داد", "k2-3", size=17, color=C["ink"], tag="h4"), button("مطالعه", SLUG["post"], "k2-3b", bg=C["royal"], color=C["white"])], 33)], "k2-r"),
    ]),
]

BODIES["post"] = [
    hero("رونمایی از هیوندای الانترا ۲۰۲۷؛ بزرگ‌تر، لوکس‌تر و مجهز به فناوری‌های نوین",
         "تغییرات گسترده در نسل جدید هیوندای الانترا.", "بازگشت به بلاگ", SLUG["blog"], "t1"),
    section(seed="t2", elements=[
        heading("تغییرات گسترده در نسل جدید هیوندای الانترا", "t2-h", color=C["ink"], size=28),
        text("هیوندای الانترا ۲۰۲۷ با طراحی جدید، ابعاد بزرگ‌تر و امکانات فناورانه‌تر معرفی شد.", "t2-t"),
    ]),
    section(seed="t3", elements=[
        heading("هیوندای الانترا جدید عضلانی‌تر می‌شود", "t3-h", color=C["ink"], size=28),
        text("در این نسل، فرم بدنه اسپرت‌تر شده و از پیشرانه‌های بهینه‌تر بهره می‌برد.", "t3-t"),
    ]),
    section(bg=C["mist"], seed="t4", elements=[
        heading("تازه‌های تکنولوژی", "t4-h", color=C["ink"], size=24),
        text("پیلار کلاستر چیست؟ استراتژی هوشمندانه برای افزایش ترافیک و بهبود سئو", "t4-t"),
        button("مطالعه بیشتر", SLUG["blog"], "t4-b", bg=C["royal"], color=C["white"]),
    ]),
]

BODIES["shop"] = [
    hero("محصولات با تخفیف استثنایی", "دوره‌های آموزشی، محصولات دیجیتال و پکیج‌های استودیو اثر.", "مشاهده محصولات", SLUG["shop"] + "#products", "s1"),
    section(seed="s2", elements=[
        heading("محصولات", "s2-h", color=C["ink"]),
        row([([heading("پگ بورد رو میزی", "s2-1", size=18, color=C["ink"], tag="h3"), image("product-pegboard", "s2-1i", alt="پگ بورد رو میزی", radius_px=12), text("قیمت: ۲,۴۹۸,۰۰۰ تومان", "s2-1p", size=14), button("مشاهده", SLUG["product"], "s2-1b", bg=C["amber"], color=C["ink"])], 33),
             ([heading("پگ بورد رو میزی", "s2-2", size=18, color=C["ink"], tag="h3"), text("قیمت: ۲,۴۹۸,۰۰۰ تومان", "s2-2p", size=14), button("مشاهده", SLUG["product"], "s2-2b", bg=C["amber"], color=C["ink"])], 33),
             ([heading("پگ بورد رو میزی", "s2-3", size=18, color=C["ink"], tag="h3"), text("قیمت: ۲,۴۹۸,۰۰۰ تومان", "s2-3p", size=14), button("مشاهده", SLUG["product"], "s2-3b", bg=C["amber"], color=C["ink"])], 33)], "s2-r"),
    ]),
    section(seed="s3", elements=[
        heading("پرسش‌های پرتکرار", "s3-h", color=C["ink"]),
        text("سوالات متداول درباره خرید و ارسال سفارش.", "s3-t"),
    ]),
]

BODIES["product"] = [
    hero("پگ بورد رو میزی", "ابزار منظم‌سازی میز کار با طراحی مدرن.", "افزودن به سبد", SLUG["product"], "r1"),
    section(seed="r2", elements=[
        heading("توضیحات محصول", "r2-h", color=C["ink"]),
        image("product-pegboard", "r2-img", alt="پگ بورد رو میزی", max_w=520, radius_px=16),
        text("پگ بورد رو میزی استودیو اثر برای سازمان‌دهی ابزار و لوازم روی میز کار طراحی شده است.", "r2-t"),
        text("قیمت: ۲,۴۹۸,۰۰۰ تومان", "r2-p", size=18, color=C["royal"], weight="700"),
    ]),
    section(bg=C["mist"], seed="r3", elements=[
        heading("محصولات مرتبط", "r3-h", color=C["ink"], size=28),
        row([([heading("پگ بورد رو میزی", "r3-1", size=18, color=C["ink"], tag="h3"), button("مشاهده", SLUG["product"], "r3-1b", bg=C["amber"], color=C["ink"])], 33),
             ([heading("پگ بورد رو میزی", "r3-2", size=18, color=C["ink"], tag="h3"), button("مشاهده", SLUG["product"], "r3-2b", bg=C["amber"], color=C["ink"])], 33),
             ([heading("پگ بورد رو میزی", "r3-3", size=18, color=C["ink"], tag="h3"), button("مشاهده", SLUG["product"], "r3-3b", bg=C["amber"], color=C["ink"])], 33)], "r3-r"),
    ]),
]

BODIES["course"] = [
    hero("دوره جامع فتوشاپ", "آموزش کامل فتوشاپ از مقدماتی تا پیشرفته.", "ثبت‌نام در دوره", SLUG["course"] + "#curriculum", "d1"),
    section(seed="d2", elements=[
        heading("توضیحات دوره", "d2-h", color=C["ink"]),
        image("course-photoshop-intro", "d2-img", alt="معرفی دوره جامع فتوشاپ", max_w=560, radius_px=16),
        text("در این دوره، اصول و تکنیک‌های طراحی گرافیک در فتوشاپ را از پایه یاد می‌گیرید.", "d2-t"),
    ]),
    section(bg=C["mist"], seed="d3", elements=[
        heading("آنچه در دوره آموزش جامع فتوشاپ خواهید دید:", "d3-h", color=C["ink"], size=28),
        text("مبانی فتوشاپ، روتوش تصویر، طراحی پوستر، کار با لایه‌ها و ماسک، خروجی حرفه‌ای.", "d3-t"),
    ]),
    section(seed="d4", elements=[
        heading("گواهینامه پایان دوره آکادمی اثر", "d4-h", color=C["ink"], size=28),
        image("course-certificate", "d4-img", alt="گواهینامه پایان دوره آکادمی اثر", max_w=420, radius_px=16),
        text("پس از پایان دوره، گواهینامه معتبر آکادمی اثر دریافت می‌کنید.", "d4-t"),
    ]),
    section(seed="d5", elements=[
        heading("دوره‌های مرتبط", "d5-h", color=C["ink"]),
        row([([heading("دوره جامع Cinema 4D", "d5-1", size=18, color=C["ink"], tag="h3"), button("مشاهده", SLUG["course"], "d5-1b", bg=C["amber"], color=C["ink"])], 33),
             ([heading("دوره جامع Cinema 4D", "d5-2", size=18, color=C["ink"], tag="h3"), button("مشاهده", SLUG["course"], "d5-2b", bg=C["amber"], color=C["ink"])], 33),
             ([heading("دوره جامع Cinema 4D", "d5-3", size=18, color=C["ink"], tag="h3"), button("مشاهده", SLUG["course"], "d5-3b", bg=C["amber"], color=C["ink"])], 33)], "d5-r"),
    ]),
]

# ======================================================================
# خروجی ۱: قالب‌های المنتور (فقط بدنه) — برای ایمپورت دستی
# ======================================================================
ET_DIR = os.path.join(BASE, "elementor-templates")
os.makedirs(ET_DIR, exist_ok=True)
for meta in PAGES:
    key = meta["key"]
    tpl = {"title": meta["title"], "type": "page", "version": "0.4",
           "page_settings": [], "content": BODIES[key]}
    with open(os.path.join(ET_DIR, "effect-studio-%s.json" % key), "w", encoding="utf-8") as fh:
        json.dump(tpl, fh, ensure_ascii=False, indent=2)
    print("template:", "effect-studio-%s.json" % key)

# ======================================================================
# خروجی ۲: داده صفحات برای نصب خودکار (با متادیتا)
# ======================================================================
PAGES_DIR = os.path.join(BASE, "theme", "effect-studio", "inc", "pages")
os.makedirs(PAGES_DIR, exist_ok=True)
for meta in PAGES:
    key = meta["key"]
    data = dict(meta)  # slug, title, menu, front_page, posts_page
    data["content"] = BODIES[key]
    with open(os.path.join(PAGES_DIR, "%s.json" % key), "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)
    print("page-data:", "%s.json" % key)

# ======================================================================
# خروجی ۳: فایل ZIP قابل نصب قالب
# ======================================================================
THEME_DIR = os.path.join(BASE, "theme", "effect-studio")
ZIP_PATH = os.path.join(BASE, "effect-studio.zip")
if os.path.exists(ZIP_PATH):
    os.remove(ZIP_PATH)
with zipfile.ZipFile(ZIP_PATH, "w", zipfile.ZIP_DEFLATED) as zf:
    for root, dirs, files in os.walk(THEME_DIR):
        # حذف فایل‌های ناخواسته
        dirs[:] = [d for d in dirs if d not in ("__pycache__", ".git")]
        for f in files:
            full = os.path.join(root, f)
            rel = os.path.relpath(full, os.path.join(BASE, "theme"))
            zf.write(full, rel)
print("zip:", ZIP_PATH, os.path.getsize(ZIP_PATH), "bytes")

print("\nDONE: %d pages" % len(PAGES))
