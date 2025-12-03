
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

header = "## Danh mục chỉ số theo SASB\n\n"

for i in range(147, 156):
    filename = f"../docker-service/data/page_{i}.md"
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        if not content.startswith(header.strip()):
            new_content = header + content
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Added header to {filename}")
        else:
            print(f"Header already present in {filename}")
    else:
        print(f"File {filename} does not exist")