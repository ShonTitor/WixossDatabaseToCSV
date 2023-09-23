import csv
import os
import re
import requests
import time
from PIL import Image

rows = []
with open('cards_database_en.tsv', newline='', encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter="\t")
    next(reader)
    for row in reader:
        code = row[0]
        if row[2] != "PIECE":
            continue
        rows.append(row)
        #cod = re.sub(r"[-\[\]]", "", row[0])
        cod = row[0]
        row[-1] = f"https://raw.githubusercontent.com/ShonTitor/WixossImportTool/main/pieces/{cod}.jpg"
        print(row)
        path = os.path.join("images", f"{code}.jpg")
        path2 = os.path.join("pieces", f"{code}.jpg")
        if os.path.exists(path2):
            continue
        img = Image.open(path)
        img = img.rotate(-90, expand=1)
        img.save(path2, optimize=True)

"""
for row in rows:
    url = row[-1]
    r = requests.head(url)
    assert r.status_code == 200
    print(row[1])
    time.sleep(0.1)
"""

def write_file(filename, separator):
    open(filename, 'a').close()
    with open(filename, 'w', encoding="utf-8", newline='') as f:
        f.truncate()
        writer = csv.writer(f, delimiter = separator)
        header = ["code", "name", "type", "imageUrl"]
        writer.writerow(header)
        for row in rows:
            writer.writerow(row)

write_file("pieces.tsv", "\t")