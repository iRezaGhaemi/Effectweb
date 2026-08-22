# -*- coding: utf-8 -*-
"""
تولید گروه‌های فیلد ACF برای سایت «استودیو اثر» (فرمت قابل ایمپورت).
خروجی: acf-field-groups.json

نحوه استفاده:
1. ACF را فعال کنید.
2. مسیر: Custom Fields → Tools → Import Field Groups
3. این فایل JSON را آپلود کنید.

این فیلدها دقیقاً همان چیزی است که فرانت‌اند headless (lib/wp.js) می‌خواند.
"""
import json, os

BASE = os.path.dirname(os.path.abspath(__file__))

def field(key, label, name, ftype, **extra):
    base = {
        "key": key,
        "label": label,
        "name": name,
        "aria-label": "",
        "type": ftype,
        "instructions": "",
        "required": 0,
        "conditional_logic": 0,
        "wrapper": {"width": "", "class": "", "id": ""},
    }
    base.update(extra)
    return base

def text(key, label, name):
    return field(key, label, name, "text",
                 default_value="", maxlength="", placeholder="", prepend="", append="")

def textarea(key, label, name, rows=4):
    return field(key, label, name, "textarea",
                 default_value="", maxlength="", rows=rows, placeholder="", new_lines="wpautop")

def repeater(key, label, name, sub_fields, button_label="افزودن"):
    return field(key, label, name, "repeater",
                 layout="table", pagination=0, min=0, max=0, collapsed="",
                 button_label=button_label, sub_fields=sub_fields)

def group(key, title, fields, location, order=0):
    return {
        "key": key,
        "title": title,
        "fields": fields,
        "location": [location],
        "menu_order": order,
        "position": "normal",
        "style": "default",
        "label_placement": "top",
        "instruction_placement": "label",
        "hide_on_screen": "",
        "active": True,
        "description": "",
        "show_in_rest": 1,
        "modified": 0,
    }

def loc(param, value):
    return {"param": param, "operator": "==", "value": value}

# ---------- ۱) صفحه اصلی (front page) ----------
home_fields = [
    text("field_effect_home_hero_title", "عنوان هیرو", "hero_title"),
    textarea("field_effect_home_hero_subtitle", "زیرعنوان هیرو", "hero_subtitle", rows=3),
    repeater("field_effect_home_services", "خدمات", "services",
             [text("field_effect_home_service_name", "نام خدمت", "name")]),
    text("field_effect_home_stats", "آمار (متن افتخار)", "stats"),
    textarea("field_effect_home_why", "چرا اثر را انتخاب کنیم؟", "why", rows=4),
]

# ---------- ۲) درباره ما ----------
about_fields = [
    text("field_effect_about_hero", "متن هیرو", "hero_text"),
    textarea("field_effect_about_body", "متن اصلی", "body", rows=6),
]

# ---------- ۳) آکادمی ----------
academy_fields = [
    text("field_effect_academy_hero", "متن هیرو", "hero_text"),
    textarea("field_effect_academy_body", "توضیحات", "body", rows=6),
    repeater("field_effect_academy_courses", "دوره‌ها", "courses",
             [
                 text("field_effect_academy_course_title", "عنوان دوره", "title"),
                 textarea("field_effect_academy_course_desc", "توضیح دوره", "desc", rows=2),
             ]),
]

# ---------- ۴) دوره ----------
course_fields = [
    text("field_effect_course_hero", "متن هیرو", "hero_text"),
    textarea("field_effect_course_body", "توضیحات دوره", "body", rows=6),
    textarea("field_effect_course_curriculum", "سرفصل‌ها", "curriculum", rows=6),
]

groups = [
    group("group_effect_home", "صفحه اصلی — استودیو اثر", home_fields,
          [loc("page_type", "front_page")], 0),
    group("group_effect_about", "درباره ما — استودیو اثر", about_fields,
          [loc("post_type", "page")], 1),
    group("group_effect_academy", "آکادمی — استودیو اثر", academy_fields,
          [loc("post_type", "page")], 2),
    group("group_effect_course", "دوره — استودیو اثر", course_fields,
          [loc("post_type", "page")], 3),
]

out = os.path.join(BASE, "acf-field-groups.json")
with open(out, "w", encoding="utf-8") as fh:
    json.dump(groups, fh, ensure_ascii=False, indent=2)
print("OK:", out, os.path.getsize(out), "bytes,", len(groups), "groups")
