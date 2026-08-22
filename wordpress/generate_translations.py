# -*- coding: utf-8 -*-
"""
تولید فایل‌های ترجمه قالب Effect Studio:
- languages/effect-studio.pot   ← الگوی ترجمه (رشته‌های مبدأ)
- languages/fa_IR.po            ← ترجمه فارسی
- languages/fa_IR.mo            ← نسخه باینری (برای بارگذاری وردپرس)

اجرا: python3 generate_translations.py
"""
import re, glob, os, struct

BASE = os.path.dirname(os.path.abspath(__file__))
THEME = os.path.join(BASE, "theme", "effect-studio")
LANG = os.path.join(THEME, "languages")

TEXTDOMAIN = "effect-studio"

# الگوهای توابع ترجمه وردپرس
PATTERNS = [
    re.compile(r"__\(\s*['\"](.*?)['\"]\s*,\s*['\"]%s['\"]\s*\)" % TEXTDOMAIN),
    re.compile(r"_e\(\s*['\"](.*?)['\"]\s*,\s*['\"]%s['\"]\s*\)" % TEXTDOMAIN),
    re.compile(r"esc_html__\(\s*['\"](.*?)['\"]\s*,\s*['\"]%s['\"]\s*\)" % TEXTDOMAIN),
    re.compile(r"esc_html_e\(\s*['\"](.*?)['\"]\s*,\s*['\"]%s['\"]\s*\)" % TEXTDOMAIN),
    re.compile(r"esc_attr__\(\s*['\"](.*?)['\"]\s*,\s*['\"]%s['\"]\s*\)" % TEXTDOMAIN),
    re.compile(r"esc_attr_e\(\s*['\"](.*?)['\"]\s*,\s*['\"]%s['\"]\s*\)" % TEXTDOMAIN),
]


def extract_strings():
    """استخراج رشته‌ها به همراه فایل‌ها و شماره خطوط."""
    found = {}  # msgid -> {file: [lines]}
    for f in glob.glob(THEME + "/**/*.php", recursive=True):
        rel = os.path.relpath(f, THEME)
        src = open(f, encoding="utf-8").read()
        for p in PATTERNS:
            for m in p.finditer(src):
                s = m.group(1)
                line = src[: m.start()].count("\n") + 1
                found.setdefault(s, {}).setdefault(rel, []).append(line)
    return found


def po_escape(s):
    return s.replace("\\", "\\\\").replace('"', '\\"')


def write_pot(found):
    lines = []
    lines.append('# Copyright (C) 2026 Effect Studio')
    lines.append('# This file is distributed under the GPLv2 or later.')
    lines.append('msgid ""')
    lines.append('msgstr ""')
    lines.append('"Project-Id-Version: Effect Studio 1.0.0\\n"')
    lines.append('"Report-Msgid-Bugs-To: https://github.com/iRezaGhaemi/Effectweb\\n"')
    lines.append('"POT-Creation-Date: 2026-08-22 00:00+0330\\n"')
    lines.append('"PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE\\n"')
    lines.append('"Last-Translator: FULL NAME <EMAIL@ADDRESS>\\n"')
    lines.append('"Language-Team: LANGUAGE <LL@li.org>\\n"')
    lines.append('"Language: \\n"')
    lines.append('"MIME-Version: 1.0\\n"')
    lines.append('"Content-Type: text/plain; charset=UTF-8\\n"')
    lines.append('"Content-Transfer-Encoding: 8bit\\n"')
    lines.append('"Plural-Forms: nplurals=2; plural=(n != 1);\\n"')
    lines.append('')

    for msgid in sorted(found):
        refs = found[msgid]
        for f in sorted(refs):
            for line in refs[f]:
                lines.append("#: %s:%d" % (f, line))
        lines.append('msgid "%s"' % po_escape(msgid))
        lines.append('msgstr ""')
        lines.append('')
    return "\n".join(lines)


def write_po(found):
    """ترجمه فارسی: چون رشته‌های مبدأ فارسی هستند، ترجمه یکسان است."""
    lines = []
    lines.append('# Persian translation for Effect Studio.')
    lines.append('msgid ""')
    lines.append('msgstr ""')
    lines.append('"Project-Id-Version: Effect Studio 1.0.0\\n"')
    lines.append('"Report-Msgid-Bugs-To: https://github.com/iRezaGhaemi/Effectweb\\n"')
    lines.append('"POT-Creation-Date: 2026-08-22 00:00+0330\\n"')
    lines.append('"PO-Revision-Date: 2026-08-22 00:00+0330\\n"')
    lines.append('"Last-Translator: Effect Studio <hello@effect.studio>\\n"')
    lines.append('"Language-Team: Persian <fa@li.org>\\n"')
    lines.append('"Language: fa_IR\\n"')
    lines.append('"MIME-Version: 1.0\\n"')
    lines.append('"Content-Type: text/plain; charset=UTF-8\\n"')
    lines.append('"Content-Transfer-Encoding: 8bit\\n"')
    lines.append('"Plural-Forms: nplurals=2; plural=(n != 1);\\n"')
    lines.append('')

    for msgid in sorted(found):
        refs = found[msgid]
        for f in sorted(refs):
            for line in refs[f]:
                lines.append("#: %s:%d" % (f, line))
        lines.append('msgid "%s"' % po_escape(msgid))
        # ترجمه فارسی = متن مبدأ (رشته‌ها از ابتدا فارسی نوشته شده‌اند).
        lines.append('msgstr "%s"' % po_escape(msgid))
        lines.append('')
    return "\n".join(lines)


def write_mo(found):
    """تولید فایل باینری MO استاندارد GNU gettext (برای بارگذاری وردپرس)."""
    entries = sorted(found.items())  # [(msgid, refs)]
    N = len(entries)

    orig = [k.encode("utf-8") for k, _ in entries]
    trans = [k.encode("utf-8") for k, _ in entries]  # فارسی = مبدأ

    O = 28
    T = O + N * 8
    data_start = T + N * 8

    data = b""
    orig_offsets = []
    for s in orig:
        orig_offsets.append(data_start + len(data))
        data += s + b"\x00"
    trans_offsets = []
    for s in trans:
        trans_offsets.append(data_start + len(data))
        data += s + b"\x00"

    header = struct.pack("<IIIIIII", 0x950412DE, 0, N, O, T, 0, 0)

    orig_table = b"".join(struct.pack("<II", len(s), off) for s, off in zip(orig, orig_offsets))
    trans_table = b"".join(struct.pack("<II", len(s), off) for s, off in zip(trans, trans_offsets))

    return header + orig_table + trans_table + data


def main():
    found = extract_strings()
    os.makedirs(LANG, exist_ok=True)

    pot_path = os.path.join(LANG, "%s.pot" % TEXTDOMAIN)
    po_path = os.path.join(LANG, "fa_IR.po")
    mo_path = os.path.join(LANG, "fa_IR.mo")

    with open(pot_path, "w", encoding="utf-8") as fh:
        fh.write(write_pot(found))
    with open(po_path, "w", encoding="utf-8") as fh:
        fh.write(write_po(found))
    with open(mo_path, "wb") as fh:
        fh.write(write_mo(found))

    print("POT:", pot_path, os.path.getsize(pot_path), "bytes,", len(found), "strings")
    print("PO :", po_path, os.path.getsize(po_path), "bytes")
    print("MO :", mo_path, os.path.getsize(mo_path), "bytes")


if __name__ == "__main__":
    main()
