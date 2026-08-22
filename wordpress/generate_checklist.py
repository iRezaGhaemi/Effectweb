# -*- coding: utf-8 -*-
"""
تولید چک‌لیست تست (PDF) برای بررسی قدم‌به‌قدم سایت روی هاست.
خروجی: Effect-Studio-Test-Checklist.pdf
"""
import os
import arabic_reshaper
from bidi.algorithm import get_display
from fpdf import FPDF

BASE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = "/tmp/vfont/package/fonts/ttf"

ROYAL = (74, 0, 165)
WHY = (45, 0, 101)
AMBER = (255, 170, 0)
INK = (22, 22, 29)
BODY = (61, 67, 80)
MUTED = (163, 169, 182)
LINE = (224, 226, 231)
PANEL = (250, 250, 250)
WHITE = (255, 255, 255)
GREEN = (34, 120, 60)
LILAC = (172, 138, 214)

reshaper = arabic_reshaper.ArabicReshaper(configuration={"delete_harakat": False, "support_zwj": True})


def fa(t):
    return get_display(reshaper.reshape(t))


class Checklist(FPDF):
    def __init__(self):
        super().__init__("P", "mm", "A4")
        self.set_auto_page_break(auto=True, margin=18)
        self.add_font("Vazir", "", os.path.join(FONT_DIR, "Vazirmatn-Regular.ttf"))
        self.add_font("Vazir", "B", os.path.join(FONT_DIR, "Vazirmatn-Bold.ttf"))
        self.add_font("VazirM", "", os.path.join(FONT_DIR, "Vazirmatn-Medium.ttf"))

    def header(self):
        if self.page_no() == 1:
            return
        self.set_font("VazirM", "", 8)
        self.set_text_color(*MUTED)
        self.cell(0, 8, fa("چک‌لیست تست سایت استودیو اثر"), align="R", new_x="LMARGIN", new_y="NEXT")
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

    def mc(self, w, h, text, align="R", color=None):
        if color:
            self.set_text_color(*color)
        self.multi_cell(w, h, text, align=align, new_x="LMARGIN", new_y="NEXT")

    def doc_title(self, text):
        self.set_font("Vazir", "B", 15)
        self.set_text_color(*ROYAL)
        self.mc(0, 9, fa(text), align="R")
        self.ln(2)

    def section(self, text):
        self.ln(3)
        self.set_fill_color(*WHY)
        self.set_font("Vazir", "B", 12)
        self.set_text_color(*WHITE)
        self.cell(0, 9, fa(text), fill=True, align="R", new_x="LMARGIN", new_y="NEXT")
        self.ln(2)

    def check(self, text):
        # یک آیتم چک‌لیست با باکس خالی
        self.set_font("Vazir", "", 10.5)
        self.set_text_color(*BODY)
        y = self.get_y()
        # باکس
        self.set_draw_color(*MUTED)
        self.rect(10, y, 5, 5)
        self.set_xy(18, y)
        self.mc(0, 6.5, fa(text), align="R")
        self.ln(0.5)

    def note(self, text):
        self.set_fill_color(245, 243, 255)
        self.set_draw_color(*LILAC)
        self.set_font("Vazir", "", 10)
        self.set_text_color(*BODY)
        self.mc(0, 6, fa("یادآوری: " + text), align="R")
        self.ln(2)


def build():
    pdf = Checklist()
    pdf.set_title("چک‌لیست تست سایت استودیو اثر")
    pdf.set_author("Effect Studio")

    # جلد
    pdf.add_page()
    pdf.set_fill_color(*WHY)
    pdf.rect(0, 0, 210, 297, style="F")
    pdf.set_fill_color(*AMBER)
    pdf.rect(0, 70, 210, 3, style="F")
    pdf.set_y(95)
    pdf.set_font("Vazir", "B", 28)
    pdf.set_text_color(*WHITE)
    pdf.mc(0, 14, fa("چک‌لیست تست سایت"), align="C")
    pdf.set_font("VazirM", "", 18)
    pdf.set_text_color(*LILAC)
    pdf.mc(0, 11, fa("استودیو اثر"), align="C")
    pdf.set_y(200)
    pdf.set_font("VazirM", "", 11)
    pdf.set_text_color(*MUTED)
    pdf.mc(0, 8, fa("بررسی قدم‌به‌قدم پس از استقرار روی هاست"), align="C")

    # بخش ۱: پیش‌نیازها
    pdf.add_page()
    pdf.doc_title("چک‌لیست تست — استقرار روی هاست")
    pdf.section("بخش ۱ — پیش‌نیازها")
    pdf.check("وردپرس روی هاست نصب شده و در دسترس است.")
    pdf.check("نسخه PHP حداقل ۷.۴ (ترجیحاً ۸.x) است.")
    pdf.check("افزونه المنتور نصب و فعال است.")
    pdf.check("(در صورت نیاز فروشگاه) افزونه ووکامرس نصب و فعال است.")
    pdf.check("زبان سایت روی «فارسی» تنظیم شده است.")

    # بخش ۲: نصب قالب
    pdf.section("بخش ۲ — نصب قالب Effect Studio")
    pdf.check("فایل effect-studio.zip با موفقیت آپلود/نصب شده است.")
    pdf.check("قالب Effect Studio فعال شده است.")
    pdf.check("۹ صفحه به‌صورت خودکار ساخته شده‌اند (Pages).")
    pdf.check("صفحه نخست روی «صفحه اصلی» تنظیم شده است (Settings » Reading).")
    pdf.check("منوی اصلی ساخته و به موقعیت «منوی اصلی» متصل شده است.")
    pdf.check("ساختار پیوند یکتا روی Post name است (Settings » Permalinks).")

    # بخش ۳: صفحات
    pdf.section("بخش ۳ — بررسی صفحات (هر ۹ صفحه)")
    pages = ["صفحه اصلی", "درباره ما", "آکادمی", "دوره", "بلاگ", "دسته‌بندی", "نوشته", "فروشگاه", "محصول"]
    for p in pages:
        pdf.check("صفحه «%s» بدون خطا باز می‌شود." % p)
    pdf.note("اگر صفحه‌ای خالی بود: المنتور فعال است؟ اگر نه، آن را فعال کنید و قالب را یک‌بار غیرفعال/فعال کنید. همچنین Elementor » Tools » Regenerate CSS را بزنید.")

    # بخش ۴: المنتور و ظاهر
    pdf.section("بخش ۴ — المنتور و ظاهر")
    pdf.check("صفحات با هدر و فوتر برند (بنفش تیره) نمایش داده می‌شوند.")
    pdf.check("فونت فارسی (وزیرمتن) به‌درستی بارگذاری شده است (بدون نیاز به اینترنت).")
    pdf.check("متن‌ها راست‌چین هستند.")
    pdf.check("رنگ‌های برند (بنفش #4a00a5، کهربایی #ffaa00) درست نمایش داده می‌شوند.")
    pdf.check("تصاویر (دوره‌ها، محصول، تیم) نمایش داده می‌شوند.")
    pdf.check("دکمه‌ها به صفحات درست لینک شده‌اند.")
    pdf.check("در موبایل، منوی همبرگری باز و بسته می‌شود.")
    pdf.check("اگر ووکامرس فعال است: صفحه فروشگاه و محصول با استایل برند نمایش داده می‌شوند.")

    # بخش ۵: لینک‌ها
    pdf.section("بخش ۵ — لینک‌ها و ناوبری")
    pdf.check("لینک «درباره ما» به صفحه درباره ما می‌رود.")
    pdf.check("لینک «بلاگ» به صفحه بلاگ می‌رود.")
    pdf.check("لینک «فروشگاه» به صفحه فروشگاه می‌رود.")
    pdf.check("لینک «آکادمی هوش مصنوعی» به صفحه آکادمی می‌رود.")
    pdf.check("لینک «ارتباط با ما» به بخش تماس می‌رود.")
    pdf.check("هیچ لینک شکسته (404) در صفحات اصلی وجود ندارد.")

    # بخش ۶: عملکرد
    pdf.section("بخش ۶ — عملکرد و سرعت")
    pdf.check("صفحه اصلی در کمتر از ۳ ثانیه لود می‌شود.")
    pdf.check("تصاویر بدون خطا لود می‌شوند.")
    pdf.check("در موبایل و دسکتاپ، چیدمان درست است (تست واکنش‌گرایی).")

    # بخش ۷: نتیجه‌گیری
    pdf.section("بخش ۷ — ثبت نتیجه")
    pdf.check("تمام موارد بالا بررسی و تأیید شد.")
    pdf.ln(3)
    pdf.set_font("Vazir", "", 10.5)
    pdf.set_text_color(*BODY)
    pdf.mc(0, 7, fa("تاریخ تست: ................................"), align="R")
    pdf.mc(0, 7, fa("نام تست‌کننده: ................................"), align="R")
    pdf.mc(0, 7, fa("امضا: ................................"), align="R")

    # صفحه پایانی
    pdf.add_page()
    pdf.set_y(110)
    pdf.set_font("Vazir", "B", 20)
    pdf.set_text_color(*WHY)
    pdf.mc(0, 11, fa("هم مسیر تا تغییر"), align="C")
    pdf.set_font("VazirM", "", 12)
    pdf.set_text_color(*BODY)
    pdf.mc(0, 8, fa("استودیو اثر"), align="C")

    out = os.path.join(BASE, "Effect-Studio-Test-Checklist.pdf")
    pdf.output(out)
    print("OK:", out, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    build()
