# -*- coding: utf-8 -*-
"""
تولید PDF راهنمای راه‌اندازی سایت «استودیو اثر» (راست‌چین، فارسی).
اجرا: python3 generate_pdf.py
خروجی: Effect-Studio-Setup-Guide.pdf
"""
import os
import arabic_reshaper
from bidi.algorithm import get_display
from fpdf import FPDF

BASE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = "/tmp/vfont/package/fonts/ttf"

# ---------- رنگ‌های برند ----------
ROYAL = (74, 0, 165)
WHY = (45, 0, 101)
AMBER = (255, 170, 0)
AMBER_DARK = (232, 155, 0)
INK = (22, 22, 29)
BODY = (61, 67, 80)
MUTED = (163, 169, 182)
LINE = (224, 226, 231)
MIST = (245, 245, 245)
PANEL = (250, 250, 250)
WHITE = (255, 255, 255)
LILAC = (172, 138, 214)

reshaper = arabic_reshaper.ArabicReshaper(
    configuration={
        "delete_harakat": False,
        "support_zwj": True,
    }
)


def fa(text):
    """تبدیل متن فارسی به شکل نمایشی راست‌چین."""
    reshaped = reshaper.reshape(text)
    return get_display(reshaped)


class Guide(FPDF):
    def __init__(self):
        super().__init__(orientation="P", unit="mm", format="A4")
        self.set_auto_page_break(auto=True, margin=18)
        self.add_font("Vazir", "", os.path.join(FONT_DIR, "Vazirmatn-Regular.ttf"))
        self.add_font("Vazir", "B", os.path.join(FONT_DIR, "Vazirmatn-Bold.ttf"))
        self.add_font("VazirM", "", os.path.join(FONT_DIR, "Vazirmatn-Medium.ttf"))
        self.add_font("VazirL", "", os.path.join(FONT_DIR, "Vazirmatn-Light.ttf"))

    # ---------- multi_cell با بازنشانی موقعیت افقی (برای متن راست‌چین) ----------
    def mc(self, w, h, text, align="R", fill=False, border=0, color=None):
        if color:
            self.set_text_color(*color)
        self.multi_cell(w, h, text, align=align, fill=fill, border=border,
                        new_x="LMARGIN", new_y="NEXT")

    # ---------- helpers ----------
    def header(self):
        if self.page_no() == 1:
            return
        self.set_font("VazirM", "", 8)
        self.set_text_color(*MUTED)
        self.cell(0, 8, fa("راهنمای راه‌اندازی سایت استودیو اثر"), align="R", new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(*LINE)
        self.line(10, 14, 200, 14)
        self.set_y(18)

    def footer(self):
        if self.page_no() == 1:
            return
        self.set_y(-12)
        self.set_font("VazirM", "", 8)
        self.set_text_color(*MUTED)
        self.cell(0, 8, fa("صفحه %d" % self.page_no()), align="C")

    def heading(self, text, level=1):
        if level == 0:
            self.set_font("Vazir", "B", 20)
            self.set_text_color(*WHY)
            self.ln(2)
        elif level == 1:
            self.set_font("Vazir", "B", 15)
            self.set_text_color(*ROYAL)
            self.ln(4)
        elif level == 2:
            self.set_font("Vazir", "B", 12.5)
            self.set_text_color(*INK)
            self.ln(2)
        self.mc(0, 8, fa(text), align="R")
        self.ln(1.5)

    def para(self, text, color=BODY, size=10.5, bold=False, align="R"):
        self.set_font("Vazir", "B" if bold else "", size)
        self.set_text_color(*color)
        self.mc(0, 6.5, fa(text), align=align)
        self.ln(1)

    def bullet(self, text, color=BODY):
        self.set_font("Vazir", "", 10.5)
        self.set_text_color(*color)
        x = self.get_x()
        self.mc(0, 6.5, fa("•  " + text), align="R")
        self.ln(0.5)

    def numbered(self, num, text, color=BODY):
        self.set_font("Vazir", "", 10.5)
        self.set_text_color(*color)
        self.mc(0, 6.5, fa("%s. %s" % (num, text)), align="R")
        self.ln(0.5)

    def code_box(self, text, color=ROYAL):
        self.set_fill_color(*PANEL)
        self.set_draw_color(*LINE)
        x0 = self.get_x()
        y0 = self.get_y()
        self.set_font("Vazir", "", 9)
        self.set_text_color(*color)
        # پیش‌اندازه‌گیری تقریبی
        lines = text.split("\n")
        h = len(lines) * 5.2 + 8
        if self.get_y() + h > self.page_break_trigger:
            self.add_page()
        self.mc(0, 5.2, fa(text), align="L", fill=True, border=1)
        self.ln(2)

    def colored_bar(self, text, bg=AMBER, fg=INK):
        self.set_fill_color(*bg)
        self.set_font("Vazir", "B", 11)
        self.set_text_color(*fg)
        self.cell(0, 9, fa(text), align="R", fill=True, new_x="LMARGIN", new_y="NEXT")
        self.ln(2)

    def note(self, text):
        self.set_fill_color(245, 243, 255)
        self.set_draw_color(*LILAC)
        self.set_font("Vazir", "", 10)
        self.set_text_color(*BODY)
        self.mc(0, 6, fa("نکته: " + text), align="R", fill=True, border=1)
        self.ln(2)

    def table_row(self, cells, header=False):
        if header:
            self.set_fill_color(*WHY)
            self.set_font("Vazir", "B", 10)
            self.set_text_color(*WHITE)
        else:
            self.set_fill_color(*PANEL)
            self.set_font("Vazir", "", 10)
            self.set_text_color(*BODY)
        widths = [48, 42, 100]
        x0 = 10
        for i, c in enumerate(cells):
            self.set_xy(x0, self.get_y())
            self.cell(widths[i], 8, fa(c), border=1, fill=True, align="R")
            x0 += widths[i]
        self.ln(8)

    def color_swatch(self, hexcode, name):
        r = int(hexcode[1:3], 16)
        g = int(hexcode[3:5], 16)
        b = int(hexcode[5:7], 16)
        self.set_fill_color(r, g, b)
        self.set_draw_color(*LINE)
        self.cell(12, 12, "", fill=True, border=1)
        self.cell(3, 12, "")
        self.set_font("Vazir", "", 10)
        self.set_text_color(*BODY)
        self.cell(0, 12, fa("%s  —  %s" % (name, hexcode)), align="R", new_x="LMARGIN", new_y="NEXT")
        self.ln(1)


def build():
    pdf = Guide()
    pdf.set_title("راهنمای راه‌اندازی سایت استودیو اثر")
    pdf.set_author("Effect Studio")

    # ==================== جلد ====================
    pdf.add_page()
    pdf.set_fill_color(*WHY)
    pdf.rect(0, 0, 210, 297, style="F")

    # نوار کهربایی
    pdf.set_fill_color(*AMBER)
    pdf.rect(0, 60, 210, 3, style="F")

    pdf.set_y(80)
    pdf.set_font("Vazir", "B", 34)
    pdf.set_text_color(*WHITE)
    pdf.mc(0, 16, fa("استودیو اثر"), align="C")

    pdf.set_font("VazirM", "", 20)
    pdf.set_text_color(*LILAC)
    pdf.mc(0, 12, fa("راهنمای راه‌اندازی سایت"), align="C")

    pdf.set_y(150)
    pdf.set_font("VazirM", "", 13)
    pdf.set_text_color(*WHITE)
    pdf.mc(0, 10, fa("وردپرس فارسی  |  المنتور  |  ووکامرس"), align="C")

    pdf.set_y(175)
    pdf.set_font("VazirL", "", 11)
    pdf.set_text_color(*MUTED)
    pdf.mc(0, 8, fa("نسخه ۱.۰.۰"), align="C")

    pdf.set_y(270)
    pdf.set_font("VazirL", "", 9)
    pdf.set_text_color(*LILAC)
    pdf.mc(0, 6, fa("github.com/iRezaGhaemi/Effectweb"), align="C")

    # ==================== فهرست ====================
    pdf.add_page()
    pdf.heading("فهرست مطالب", 0)
    pdf.ln(3)
    toc = [
        "گام ۱ — نصب وردپرس فارسی",
        "گام ۲ — نصب قالب Effect Studio و المنتور",
        "گام ۳ — فعال‌سازی راست‌چین و فونت فارسی",
        "گام ۳.۵ — فروشگاه با ووکامرس",
        "گام ۴ — ایمپورت قالب‌های المنتور",
        "گام ۵ — اتصال صفحات (لینک‌ها)",
        "گام ۶ — لوگو و تصاویر",
        "گام ۷ — منوی ناوبری",
        "رنگ‌های برند",
        "پرسش‌های متداول",
    ]
    for i, t in enumerate(toc, 1):
        pdf.set_font("VazirM", "", 12)
        pdf.set_text_color(*INK)
        pdf.cell(12, 10, fa(str(i)), align="R")
        pdf.set_font("Vazir", "", 12)
        pdf.set_text_color(*BODY)
        pdf.cell(0, 10, fa(t), align="R", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(5)
    pdf.note("این راهنما مکمل فایل README-fa.md در پکیج است. برای جزئیات بیشتر، همان فایل را ببینید.")

    # ==================== گام ۱ ====================
    pdf.add_page()
    pdf.heading("گام ۱ — نصب وردپرس فارسی", 1)
    pdf.para("برای شروع، باید وردپرس روی هاست نصب شده باشد. اگر هنوز نصب نکرده‌اید، از نصب‌کننده یک‌کلیکی هاست (مثل Softaculous) استفاده کنید.")
    pdf.numbered(1, "وردپرس را روی هاست نصب کنید (یا از نصب‌کننده یک‌کلیکی هاست).")
    pdf.numbered(2, "زبان فارسی را فعال کنید:")
    pdf.para("Settings  »  General  »  Site Language  »  فارسی", color=ROYAL)
    pdf.para("اگر «فارسی» در لیست نبود، از Dashboard » Updates » Install translations بسته زبان را نصب کنید.")
    pdf.numbered(3, "ساختار پیوند یکتا را روی «نام نوشته» بگذارید:")
    pdf.para("Settings  »  Permalinks  »  Post name", color=ROYAL)
    pdf.note("پیوند یکتا (Permalink) حتماً روی Post name باشد تا صفحات به‌درستی ساخته شوند.")

    # ==================== گام ۲ ====================
    pdf.heading("گام ۲ — نصب قالب Effect Studio و المنتور", 1)
    pdf.heading("۲.۱ نصب قالب اختصاصی (پیشنهادی)", 2)
    pdf.para("قالب Effect Studio هدر و فوتر را دقیقاً مطابق طراحی سایت پیاده می‌کند و نیازی به Elementor Pro ندارید.")
    pdf.colored_bar("روش ۱ — آپلود مستقیم ZIP (ساده‌تر)")
    pdf.numbered(1, "فایل theme/effect-studio.zip را از مسیر زیر آپلود و نصب کنید:")
    pdf.para("Appearance  »  Themes  »  Add New  »  Upload Theme", color=ROYAL)
    pdf.numbered(2, "قالب Effect Studio را فعال کنید.")
    pdf.colored_bar("روش ۲ — آپلود دستی")
    pdf.numbered(1, "پوشه theme/effect-studio/ را در مسیر wp-content/themes/ هاست آپلود کنید.")
    pdf.numbered(2, "از Appearance » Themes قالب Effect Studio را فعال کنید.")
    pdf.ln(2)
    pdf.colored_bar("بعد از فعال‌سازی قالب", bg=WHY, fg=WHITE)
    pdf.bullet("۹ صفحه سایت به‌صورت خودکار ساخته می‌شوند: خانه، درباره ما، آکادمی، دوره، بلاگ، دسته‌بندی، نوشته، فروشگاه، محصول.")
    pdf.bullet("محتوای المنتور هر صفحه به‌صورت خودکار بارگذاری می‌شود (به شرط فعال بودن المنتور).")
    pdf.bullet("صفحه نخست، صفحه نوشته‌ها (بلاگ) و منوی اصلی به‌صورت خودکار تنظیم می‌شوند.")
    pdf.bullet("برای تنظیم رنگ برند، تلفن و ایمیل: Appearance » Customize » تنظیمات برند اثر.")
    pdf.ln(2)
    pdf.note("ترتیب پیشنهادی: ابتدا المنتور را نصب و فعال کنید، سپس قالب Effect Studio را فعال کنید تا محتوای صفحات درست بارگذاری شود.")

    pdf.heading("۲.۲ نصب المنتور", 2)
    pdf.numbered(1, "المنتور (نسخه رایگان کافی است) را نصب و فعال کنید:")
    pdf.para("Plugins  »  Add New  »  جستجوی Elementor  »  Install  »  Activate", color=ROYAL)

    # ==================== گام ۳ ====================
    pdf.heading("گام ۳ — فعال‌سازی راست‌چین و فونت فارسی", 1)
    pdf.para("فونت فارسی وزیرمتن به‌صورت محلی داخل قالب قرار دارد و خودکار بارگذاری می‌شود؛ نیازی به Google Fonts یا افزونه فونت نیست.")
    pdf.numbered(1, "برای راست‌چین شدن کامل، زبان سایت را روی «فارسی» بگذارید (گام ۱).")
    pdf.numbered(2, "محتوای فایل assets/effect-studio.css را در مسیر زیر قرار دهید:")
    pdf.para("Customize  »  Additional CSS", color=ROYAL)
    pdf.numbered(3, "فایل‌های فونت در theme/effect-studio/assets/fonts/Vazirmatn-*.woff2 قرار دارند.")
    pdf.note("اگر فونت دیگری (مثل ایران‌سنس) می‌خواهید، فایل woff2 آن را در همان پوشه بگذارید و @font-face را در style.css تغییر دهید.")

    # ==================== گام ۳.۵ ====================
    pdf.heading("گام ۳.۵ — فروشگاه با ووکامرس (اختیاری)", 1)
    pdf.para("اگر فروشگاه واقعی (سبد خرید و پرداخت) می‌خواهید:")
    pdf.numbered(1, "افزونه WooCommerce را نصب و فعال کنید.")
    pdf.numbered(2, "قالب Effect Studio از ووکامرس پشتیبانی می‌کند (فایل woocommerce.php و استایل اختصاصی assets/css/woocommerce.css).")
    pdf.numbered(3, "اگر صفحه‌ای با اسلاگ shop وجود داشته باشد، خودکار به‌عنوان «صفحه فروشگاه» تنظیم می‌شود.")
    pdf.numbered(4, "محصولات را از Products » Add New بسازید.")
    pdf.note("بدون ووکامرس هم صفحات فروشگاه و محصول به‌صورت نمایشی کار می‌کنند؛ اما برای سبد خرید واقعی، ووکامرس لازم است.")

    # ==================== گام ۴ ====================
    pdf.heading("گام ۴ — ایمپورت قالب‌های المنتور (اختیاری)", 1)
    pdf.para("قالب‌های المنتور فقط بدنه هستند (هدر و فوتر ندارند) تا با هدر/فوتر قالب تداخل نکنند.")
    pdf.numbered(1, "Templates » Saved Templates » Import Templates")
    pdf.numbered(2, "هر ۹ فایل JSON را یک‌جا انتخاب و ایمپورت کنید.")
    pdf.numbered(3, "صفحه جدید بسازید و Edit with Elementor را بزنید.")
    pdf.numbered(4, "در المنتور: آیکون پوشه » My Templates » قالب موردنظر » Insert.")
    pdf.note("اگر از نصب خودکار (گام ۲) استفاده کرده باشید، نیازی به این گام ندارید.")

    # ==================== گام ۵ ====================
    pdf.heading("گام ۵ — اتصال صفحات (لینک‌ها)", 1)
    pdf.para("لینک‌های داخلی به‌صورت اسلاگ نسبی نوشته شده‌اند. جدول زیر نگاشت صفحات را نشان می‌دهد:")
    pdf.ln(2)
    pdf.table_row(["صفحه", "اسلاگ پیشنهادی", "فایل قالب"], header=True)
    rows = [
        ("صفحه اصلی", "/", "effect-studio-home.json"),
        ("درباره ما", "/about-us/", "effect-studio-about-us.json"),
        ("آکادمی", "/academy/", "effect-studio-academy.json"),
        ("دوره", "/course/", "effect-studio-course.json"),
        ("بلاگ", "/blog/", "effect-studio-blog.json"),
        ("دسته‌بندی", "/blog-category/", "effect-studio-category.json"),
        ("نوشته", "/sample-post/", "effect-studio-post.json"),
        ("فروشگاه", "/shop/", "effect-studio-shop.json"),
        ("محصول", "/pegboard/", "effect-studio-product.json"),
    ]
    for r in rows:
        pdf.table_row(list(r))
    pdf.ln(2)
    pdf.note("ساده‌ترین راه جایگزینی لینک‌ها: در المنتور روی هر دکمه کلیک کنید و فیلد Link را به آدرس صفحه مربوطه تغییر دهید.")

    # ==================== گام ۶ ====================
    pdf.heading("گام ۶ — لوگو و تصاویر", 1)
    pdf.numbered(1, "لوگوی برند در assets/logo.png و assets/logo.webp موجود است.")
    pdf.numbered(2, "آن را در Media » Add New آپلود کنید.")
    pdf.numbered(3, "سایر تصاویر (نمونه‌کارها، عکس محصولات و دوره‌ها) را از فایل‌های HTML اصلی بردارید و آپلود کنید.")

    # ==================== گام ۷ ====================
    pdf.heading("گام ۷ — منوی ناوبری (اختیاری)", 1)
    pdf.numbered(1, "Appearance » Menus")
    pdf.numbered(2, "منو بسازید و آیتم‌ها را اضافه کنید: استودیو اثر، درباره ما، خدمات اثر، بلاگ، فروشگاه، ارتباط با ما.")
    pdf.numbered(3, "منو را به موقعیت «منوی اصلی» اختصاص دهید.")
    pdf.note("نصب خودکار (گام ۲) این منو را از قبل ساخته است؛ این گام فقط برای ویرایش دستی است.")

    # ==================== رنگ‌ها ====================
    pdf.add_page()
    pdf.heading("رنگ‌های برند", 1)
    pdf.para("برای هماهنگی سراسری، از این پالت استفاده کنید:")
    pdf.ln(3)
    pdf.color_swatch("#4a00a5", "بنفش اصلی (Royal)")
    pdf.color_swatch("#2d0065", "بنفش تیره (هدر/فوتر)")
    pdf.color_swatch("#6e33b7", "بنفش میانی")
    pdf.color_swatch("#ac8ad6", "بنفش روشن (Lilac)")
    pdf.color_swatch("#ffaa00", "کهربایی (CTA)")
    pdf.color_swatch("#16161d", "متن اصلی (Ink)")
    pdf.color_swatch("#3d4350", "متن بدنه (Body)")
    pdf.ln(4)
    pdf.heading("فونت", 2)
    pdf.para("وزیرمتن (Vazirmatn) — به‌صورت محلی داخل قالب، بدون نیاز به Google Fonts.")

    # ==================== FAQ ====================
    pdf.heading("پرسش‌های متداول", 1)
    pdf.heading("آیا قالب‌ها بدون Elementor Pro کار می‌کنند؟", 2)
    pdf.para("بله. همه ویجت‌های استفاده‌شده (Heading، Text Editor، Button، Image، Spacer، Divider) در نسخه رایگان موجودند.")
    pdf.heading("چرا لینک‌ها اول # یا / هستند؟", 2)
    pdf.para("این‌ها اسلاگ‌های نسبی وردپرس هستند که بعد از ساخت صفحات به لینک نهایی اشاره می‌کنند (جدول گام ۵).")
    pdf.heading("آیا فونت نیاز به اینترنت دارد؟", 2)
    pdf.para("خیر. فونت وزیرمتن به‌صورت محلی داخل قالب است و آفلاین کار می‌کند.")
    pdf.heading("چرا وردپرس فقط با انداختن ZIP راه نمی‌افتد؟", 2)
    pdf.para("وردپرس باید از قبل نصب باشد؛ این ZIP یک پکیج قالب + صفحات است که بعد از نصب وردپرس، سایت را با یک کلیک می‌سازد.")

    # ==================== صفحه پایانی ====================
    pdf.add_page()
    pdf.set_y(110)
    pdf.set_font("Vazir", "B", 22)
    pdf.set_text_color(*WHY)
    pdf.mc(0, 12, fa("هم مسیر تا تغییر"), align="C")
    pdf.set_font("VazirM", "", 13)
    pdf.set_text_color(*BODY)
    pdf.mc(0, 9, fa("استودیو اثر"), align="C")
    pdf.ln(6)
    pdf.set_font("VazirL", "", 10)
    pdf.set_text_color(*MUTED)
    pdf.mc(0, 7, fa("۰۹۱۵ ۳۸۹ ۲۰۸۸   |   hello@effect.studio"), align="C")

    out = os.path.join(BASE, "Effect-Studio-Setup-Guide.pdf")
    pdf.output(out)
    print("OK:", out, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    build()
