import os
import json
import re
from pathlib import Path

import re

import unicodedata
# VietnameseToneNormalization.md
# https://github.com/VinAIResearch/BARTpho/blob/main/VietnameseToneNormalization.md

TONE_NORM_VI = {
    'òa': 'oà', 'Òa': 'Oà', 'ÒA': 'OÀ',\
    'óa': 'oá', 'Óa': 'Oá', 'ÓA': 'OÁ',\
    'ỏa': 'oả', 'Ỏa': 'Oả', 'ỎA': 'OẢ',\
    'õa': 'oã', 'Õa': 'Oã', 'ÕA': 'OÃ',\
    'ọa': 'oạ', 'Ọa': 'Oạ', 'ỌA': 'OẠ',\
    'òe': 'oè', 'Òe': 'Oè', 'ÒE': 'OÈ',\
    'óe': 'oé', 'Óe': 'Oé', 'ÓE': 'OÉ',\
    'ỏe': 'oẻ', 'Ỏe': 'Oẻ', 'ỎE': 'OẺ',\
    'õe': 'oẽ', 'Õe': 'Oẽ', 'ÕE': 'OẼ',\
    'ọe': 'oẹ', 'Ọe': 'Oẹ', 'ỌE': 'OẸ',\
    'ùy': 'uỳ', 'Ùy': 'Uỳ', 'ÙY': 'UỲ',\
    'úy': 'uý', 'Úy': 'Uý', 'ÚY': 'UÝ',\
    'ủy': 'uỷ', 'Ủy': 'Uỷ', 'ỦY': 'UỶ',\
    'ũy': 'uỹ', 'Ũy': 'Uỹ', 'ŨY': 'UỸ',\
    'ụy': 'uỵ', 'Ụy': 'Uỵ', 'ỤY': 'UỴ'
    }

def normalize_vnese(text):
    for i, j in TONE_NORM_VI.items():
        text = text.replace(i, j)
    # Remove control characters (ASCII 0–31, plus DEL 127)
    text = re.sub(r'[\x00-\x1F\x7F]', '', text)
    # normalize spacing
    text = text.replace('\xa0', ' ')
    # Normalize input text to NFC
    text = unicodedata.normalize("NFC", text)
    return text

import os


def numeric_key(filename):
    m = re.search(r'(\d+)', filename)
    if m:
        return int(m.group(1))
    return filename

def main():
    data_dir = Path("../docker-service/data")
    json_dir = data_dir / "json"
    json_dir.mkdir(exist_ok=True)

    md_files = sorted([f for f in data_dir.glob("*.md")], key=lambda x: numeric_key(x.name))

    pages = []
    ind = 1
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            ind += 1
            pages.append({
                "page": ind,
                "content": normalize_vnese(content)
            })
        except Exception as e:
            print(f"Error reading {md_file}: {e}")

    output_file = json_dir / "all_md.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump({"pages": pages}, f, ensure_ascii=False, indent=2)

    print(f"Converted {len(pages)} files to {output_file}")

if __name__ == "__main__":
    main()