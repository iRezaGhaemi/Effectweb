# -*- coding: utf-8 -*-
"""
تولید قالب‌های قابل-ایمپورت المنتور برای سایت «استودیو اثر»
خروجی: فایل‌های JSON در پوشه elementor-templates/
هر فایل را می‌توان از مسیر قالب‌ها (Templates) > ذخیره‌شده > ایمپورت کرد.
"""
import json, hashlib, os

# ---------- برند ----------
C = {
    "royal": "#4a00a5", "royal2": "#5e01a4", "violet": "#6e33b7",
    "lilac": "#ac8ad6", "why": "#2d0065", "amber": "#FFAA00",
    "amberDark": "#e89b00", "ink": "#16161d", "body": "#3d4350",
    "panel": "#fafafa", "mist": "#f5f5f5", "line": "#e0e2e7",
    "white": "#ffffff",
}

# اسلاگ صفحات وردپرس (برای لینک‌های داخلی)
SLUG = {
    "home": "/", "about": "/about-us/", "academy": "/academy/",
    "course": "/academy/course/", "blog": "/blog/",
    "category": "/category/technology/", "post": "/blog/hyundai-elantra-2027/",
    "shop": "/shop/", "product": "/shop/pegboard/",
}

def uid(seed):
    return hashlib.md5(seed.encode("utf-8")).hexdigest()[:8]

def w(widgetType, settings, seed, elements=None):
    return {"id": uid(seed), "elType": "widget", "widgetType": widgetType,
            "isInner": False, "settings": settings, "elements": elements or []}

def box(settings, elements, seed):
    return {"id": uid(seed), "elType": "container", "isInner": False,
            "settings": settings, "elements": elements}

def pad(v, unit="px"):
    return {"unit": unit, "top": str(v), "right": str(v), "bottom": str(v), "left": str(v), "isLinked": True}

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
    return w("text-editor", {
        "editor": html, "align": align, "text_color": color,
        "typography_typography": "custom",
        "typography_font_size": {"unit": "px", "size": size, "sizes": []},
        "typography_font_weight": weight,
        "typography_line_height": {"unit": "em", "size": line, "sizes": []},
    }, seed)

def button(text_, url, seed, bg=C["amber"], color=C["ink"], size=16, rd=12, weight="600", align="right"):
    return w("button", {
        "text": text_, "align": align,
        "link": {"url": url, "is_external": "", "nofollow": "", "custom_attributes": ""},
        "background_color": bg, "button_text_color": color,
        "border_radius": radius(rd),
        "typography_typography": "custom",
        "typography_font_size": {"unit": "px", "size": size, "sizes": []},
        "typography_font_weight": weight,
        "button_box_shadow_box_shadow_type": "",
    }, seed)

def spacer(h, seed):
    return w("spacer", {"space": {"unit": "px", "size": h, "sizes": []}}, seed)

def divider(seed, color=C["line"], wpx=1):
    return w("divider", {"color": color, "weight": {"unit": "px", "size": wpx, "sizes": []}}, seed)

def section(bg=None, elements=None, seed="s", pt=60, pb=60, px=20, radius_px=0, gap=20):
    s = {"padding": {"unit": "px", "top": str(pt), "right": str(px), "bottom": str(pb),
                     "left": str(px), "isLinked": False}, "gap": {"unit": "px", "size": gap, "sizes": []}}
    if bg:
        s["background_background"] = "classic"
        s["background_color"] = bg
    if radius_px:
        s["border_radius"] = radius(radius_px)
    return box(s, elements or [], seed)

def row(cols, seed, gap=20, valign="center"):
    # هر آیتم cols: (elements, width_percent)
    els = []
    for i, (e, width) in enumerate(cols):
        els.append(box({"width": {"unit": "%", "size": width, "sizes": []},
                        "flex_direction": "column", "align_items": "stretch"},
                       e, seed + "-c%d" % i))
    return box({"flex_direction": "row", "gap": {"unit": "px", "size": gap, "sizes": []},
                "align_items": valign}, els, seed)

# ---------- هدر و فوتر مشترک ----------
NAV = [
    ("استودیو اثر", SLUG["home"]), ("درباره ما", SLUG["about"]),
    ("خدمات اثر", SLUG["home"] + "#services"), ("بلاگ", SLUG["blog"]),
    ("فروشگاه", SLUG["shop"]), ("ارتباط با ما", SLUG["home"] + "#contact"),
]

def header(seed):
    nav_html = " ".join(
        '<a href="%s" style="color:%s;text-decoration:none;margin-inline-end:22px;font-size:15px;font-weight:500;">%s</a>'
        % (u, C["lilac"], t) for t, u in NAV)
    logo = w("image", {"image": {"url": "LOGO_URL", "id": "", "size": "full", "alt": "استودیو اثر"},
                       "width": {"unit": "px", "size": 130, "sizes": []}, "align": "right"}, seed + "-logo")
    nav = text('<div dir="rtl" style="display:flex;flex-wrap:wrap;align-items:center;">%s</div>' % nav_html,
               seed + "-nav", color=C["white"], size=15)
    cta = button("آکادمی هوش مصنوعی", SLUG["academy"], seed + "-cta", bg=C["amber"], color=C["ink"], size=15)
    inner = row([([logo], 20), ([nav], 60), ([cta], 20)], seed + "-hrow", gap=12)
    return box({"background_background": "classic", "background_color": C["why"],
                "padding": pad(14), "border_radius": radius(18)}, [inner], seed)

def footer(seed):
    col1 = [heading("خدمات اثر", seed + "-f1h", size=16, color=C["white"], tag="h4"),
            text('<a href="%s" style="color:#d0d0d2;">طراحی سایت و اپلیکیشن</a><br>'
                 '<a href="%s" style="color:#d0d0d2;">هویت بصری</a><br>'
                 '<a href="%s" style="color:#d0d0d2;">سوشال مدیا</a><br>'
                 '<a href="%s" style="color:#d0d0d2;">مارکتینگ و سئو</a>'
                 % (SLUG["home"] + "#services", SLUG["home"] + "#services",
                    SLUG["home"] + "#services", SLUG["home"] + "#services"),
                 seed + "-f1", color=C["body"], size=14)]
    col2 = [heading("دسترسی آسان", seed + "-f2h", size=16, color=C["white"], tag="h4"),
            text('<a href="%s" style="color:#d0d0d2;">صفحه اصلی</a><br>'
                 '<a href="%s" style="color:#d0d0d2;">فروشگاه</a><br>'
                 '<a href="%s" style="color:#d0d0d2;">مقالات</a><br>'
                 '<a href="%s" style="color:#d0d0d2;">ارتباط با ما</a>'
                 % (SLUG["home"], SLUG["shop"], SLUG["blog"], SLUG["home"] + "#contact"), seed + "-f2", color=C["body"], size=14)]
    col3 = [heading("ارتباط با ما", seed + "-f3h", size=16, color=C["white"], tag="h4"),
            text('۰۹۱۵ ۳۸۹ ۲۰۸۸<br>hello@effect.studio', seed + "-f3", color=C["lilac"], size=15)]
    col4 = [heading("آکادمی اثر", seed + "-f4h", size=16, color=C["white"], tag="h4"),
            text('<a href="%s" style="color:#d0d0d2;">دوره‌های آموزشی</a><br>'
                 '<a href="%s" style="color:#d0d0d2;">مقالات آموزشی</a>'
                 % (SLUG["academy"], SLUG["blog"]), seed + "-f4", color=C["body"], size=14)]
    cols = row([(col1, 25), (col2, 25), (col3, 25), (col4, 25)], seed + "-frow", gap=16, valign="flex-start")
    copyr = text('<div dir="rtl" style="text-align:center;color:#fff;">تمام حقوق برای استودیو اثر محفوظ می‌باشد. | Effect Studio 2025</div>',
                 seed + "-copy", color=C["white"], size=13, align="center")
    return box({"background_background": "classic", "background_color": C["why"],
                "padding": pad(30)}, [cols, spacer(20, seed + "-fsp"), divider(seed + "-fd", color="#430096"),
                                      copyr], seed)

def build(title, sections, seed):
    content = [header(seed + "-hdr")] + sections + [footer(seed + "-ftr")]
    return {"title": title, "type": "page", "version": "0.4", "page_settings": [], "content": content}

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
# ۱) صفحه اصلی
# ======================================================================
home = [
    hero("هم مسیر تا تغییر",
         "خدمات حرفه‌ای تولید محتوا، طراحی سایت، طراحی اپلیکیشن، طراحی لوگو، طراحی هویت برند و طراحی‌های چاپی.",
         "مشاوره رایگان", SLUG["home"] + "#contact", "p1",
         cta2=("مشاهده خدمات", SLUG["home"] + "#services")),
    section(seed="p2", elements=[
        heading("خدمات آژانس دیجیتال اثر", "p2-h", color=C["ink"]),
        text("طراحی سایت و اپلیکیشن، هویت بصری، سوشال مدیا، مارکتینگ، سئو و تبلیغات — راهکارهای اختصاصی برای هر کسب‌وکار.", "p2-t"),
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
write_home = build("صفحه اصلی - استودیو اثر", home, "home")

# ======================================================================
# ۲) درباره ما
# ======================================================================
about = [
    hero("درباره استودیو اثر", "تیم حرفه‌ای و خلاق افکت؛ همراه شما از ایده تا اجرا.", "همکاری با ما", SLUG["home"] + "#contact", "a1"),
    section(seed="a2", elements=[
        heading("تیم حرفه‌ای و خلاق افکت", "a2-h", color=C["ink"]),
        text("استودیو اثر با تیمی متخصص در طراحی، برنامه‌نویسی و بازاریابی دیجیتال، به کسب‌وکارها کمک می‌کند تا برند خود را بسازند و رشد کنند.", "a2-t"),
    ]),
    section(bg=C["mist"], seed="a3", elements=[
        heading("مفتخر به همکاری با بیش از ۱۰۰ استارتاپ و بیزنس‌های موفق", "a3-h", color=C["ink"], size=32),
    ]),
    section(seed="a4", elements=[
        heading("پرسش‌های پرتکرار", "a4-h", color=C["ink"]),
        text("پاسخ سوالات متداول درباره خدمات و همکاری با استودیو اثر.", "a4-t"),
    ]),
]
write_about = build("درباره ما - استودیو اثر", about, "about")

# ======================================================================
# ۳) آکادمی
# ======================================================================
academy = [
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
        text("آموزش جامع نرم‌افزار سینما فوردی برای طراحی سه‌بعدی و موشن گرافیک.", "c3-t"),
        button("مشاهده دوره", SLUG["course"], "c3-b", bg=C["amber"], color=C["ink"]),
    ]),
    section(seed="c4", elements=[
        heading("دوره جامع فتوشاپ", "c4-h", color=C["ink"], size=26, tag="h3"),
        text("آموزش کامل فتوشاپ از مقدماتی تا پیشرفته برای طراحان.", "c4-t"),
        button("مشاهده دوره", SLUG["course"], "c4-b", bg=C["amber"], color=C["ink"]),
    ]),
    section(seed="c5", elements=[
        heading("نظرات مشتریان", "c5-h", color=C["ink"]),
        text("دانشجویان و کارفرمایان درباره دوره‌های آکادمی اثر چه می‌گویند.", "c5-t"),
    ]),
]
write_academy = build("آکادمی - استودیو اثر", academy, "academy")

# ======================================================================
# ۴) بلاگ
# ======================================================================
blog = [
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
write_blog = build("بلاگ - استودیو اثر", blog, "blog")

# ======================================================================
# ۵) دسته‌بندی بلاگ
# ======================================================================
category = [
    hero("دسته‌بندی: تکنولوژی", "آخرین مطالب و اخبار حوزه تکنولوژی.", "داغ‌ترین مطالب", SLUG["category"], "k1"),
    section(seed="k2", elements=[
        heading("داغ‌ترین مطالب این دسته", "k2-h", color=C["ink"]),
        row([([heading("پیلار کلاستر چیست؟ استراتژی هوشمندانه برای افزایش ترافیک و بهبود سئو", "k2-1", size=17, color=C["ink"], tag="h4"), button("مطالعه", SLUG["post"], "k2-1b", bg=C["royal"], color=C["white"])], 33),
             ([heading("رونمایی از هیوندای الانترا ۲۰۲۷", "k2-2", size=17, color=C["ink"], tag="h4"), button("مطالعه", SLUG["post"], "k2-2b", bg=C["royal"], color=C["white"])], 33),
             ([heading("فاز جدید جنگ فناوری: آمریکا ممنوعیت‌های واردات تجهیزات چینی را افزایش داد", "k2-3", size=17, color=C["ink"], tag="h4"), button("مطالعه", SLUG["post"], "k2-3b", bg=C["royal"], color=C["white"])], 33)], "k2-r"),
    ]),
]
write_category = build("دسته‌بندی - استودیو اثر", category, "category")

# ======================================================================
# ۶) نوشته بلاگ
# ======================================================================
post = [
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
write_post = build("نوشته بلاگ - استودیو اثر", post, "post")

# ======================================================================
# ۷) فروشگاه
# ======================================================================
shop = [
    hero("محصولات با تخفیف استثنایی", "دوره‌های آموزشی، محصولات دیجیتال و پکیج‌های استودیو اثر.", "مشاهده محصولات", SLUG["shop"] + "#products", "s1"),
    section(seed="s2", elements=[
        heading("محصولات", "s2-h", color=C["ink"]),
        row([([heading("پگ بورد رو میزی", "s2-1", size=18, color=C["ink"], tag="h3"), text("قیمت: ۲,۴۹۸,۰۰۰ تومان", "s2-1p", size=14), button("مشاهده", SLUG["product"], "s2-1b", bg=C["amber"], color=C["ink"])], 33),
             ([heading("پگ بورد رو میزی", "s2-2", size=18, color=C["ink"], tag="h3"), text("قیمت: ۲,۴۹۸,۰۰۰ تومان", "s2-2p", size=14), button("مشاهده", SLUG["product"], "s2-2b", bg=C["amber"], color=C["ink"])], 33),
             ([heading("پگ بورد رو میزی", "s2-3", size=18, color=C["ink"], tag="h3"), text("قیمت: ۲,۴۹۸,۰۰۰ تومان", "s2-3p", size=14), button("مشاهده", SLUG["product"], "s2-3b", bg=C["amber"], color=C["ink"])], 33)], "s2-r"),
    ]),
    section(seed="s3", elements=[
        heading("پرسش‌های پرتکرار", "s3-h", color=C["ink"]),
        text("سوالات متداول درباره خرید و ارسال سفارش.", "s3-t"),
    ]),
]
write_shop = build("فروشگاه - استودیو اثر", shop, "shop")

# ======================================================================
# ۸) صفحه محصول
# ======================================================================
product = [
    hero("پگ بورد رو میزی", "ابزار منظم‌سازی میز کار با طراحی مدرن.", "افزودن به سبد", SLUG["product"], "r1"),
    section(seed="r2", elements=[
        heading("توضیحات محصول", "r2-h", color=C["ink"]),
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
write_product = build("محصول - استودیو اثر", product, "product")

# ======================================================================
# ۹) صفحه دوره
# ======================================================================
course = [
    hero("دوره جامع فتوشاپ", "آموزش کامل فتوشاپ از مقدماتی تا پیشرفته.", "ثبت‌نام در دوره", SLUG["course"] + "#curriculum", "d1"),
    section(seed="d2", elements=[
        heading("توضیحات دوره", "d2-h", color=C["ink"]),
        text("در این دوره، اصول و تکنیک‌های طراحی گرافیک در فتوشاپ را از پایه یاد می‌گیرید.", "d2-t"),
    ]),
    section(bg=C["mist"], seed="d3", elements=[
        heading("آنچه در دوره آموزش جامع فتوشاپ خواهید دید:", "d3-h", color=C["ink"], size=28),
        text("مبانی فتوشاپ، روتوش تصویر، طراحی پوستر، کار با لایه‌ها و ماسک، خروجی حرفه‌ای.", "d3-t"),
    ]),
    section(seed="d4", elements=[
        heading("گواهینامه پایان دوره آکادمی اثر", "d4-h", color=C["ink"], size=28),
        text("پس از پایان دوره، گواهینامه معتبر آکادمی اثر دریافت می‌کنید.", "d4-t"),
    ]),
    section(seed="d5", elements=[
        heading("دوره‌های مرتبط", "d5-h", color=C["ink"]),
        row([([heading("دوره جامع Cinema 4D", "d5-1", size=18, color=C["ink"], tag="h3"), button("مشاهده", SLUG["course"], "d5-1b", bg=C["amber"], color=C["ink"])], 33),
             ([heading("دوره جامع Cinema 4D", "d5-2", size=18, color=C["ink"], tag="h3"), button("مشاهده", SLUG["course"], "d5-2b", bg=C["amber"], color=C["ink"])], 33),
             ([heading("دوره جامع Cinema 4D", "d5-3", size=18, color=C["ink"], tag="h3"), button("مشاهده", SLUG["course"], "d5-3b", bg=C["amber"], color=C["ink"])], 33)], "d5-r"),
    ]),
]
write_course = build("دوره - استودیو اثر", course, "course")

# ---------- خروجی ----------
OUT = os.path.join(os.path.dirname(__file__), "elementor-templates")
os.makedirs(OUT, exist_ok=True)
templates = {
    "home": write_home, "about-us": write_about, "academy": write_academy,
    "blog": write_blog, "category": write_category, "post": write_post,
    "shop": write_shop, "product": write_product, "course": write_course,
}
for name, obj in templates.items():
    # آدرس لوگو در وردپرس بعداً توسط کاربر جایگزین می‌شود
    fn = os.path.join(OUT, "effect-studio-%s.json" % name)
    with open(fn, "w", encoding="utf-8") as fh:
        json.dump(obj, fh, ensure_ascii=False, indent=2)
    print("wrote", fn)

print("DONE:", len(templates), "templates")
