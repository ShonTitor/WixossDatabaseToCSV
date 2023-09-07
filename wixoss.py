import requests
import json
import csv
import time
import sys
import os
import io
from PIL import Image

SAVE_IMAGES = True
cards = {}

rarity_url = "https://www.takaratomy.co.jp/products/en.wixoss/card/master.php?m=rarity"
rarities: set = set()

r = requests.get(rarity_url)
rarity_data = json.loads(r.content)
rarity_suffix = {
    item["name"]:item["image_end"]
    for item in rarity_data["items"]
}

#rarity_suffix = {'PI': '', 'SR': '', 'L': '', 'L(P)': 'P[EN]', 'R': '', 'R(P)': 'P[EN]', "R(P')": 'PS[EN]', 'C': '', 'C(P)': 'P[EN]', 'ST': '', 'ST(P)': 'P[EN]', 'PR': '', 'PR(P)': 'P[EN]', '???': '', 'DiR': 'D[EN]', 'SCR': 'S[EN]', 'LC': '', 'LC(P)': 'P[EN]', 'LR': 'R[EN]', 'LRP': 'P[EN]', 'SRP': 'P[EN]', 'UR': 'U[EN]', 'TK': 'P[EN]', 'Re': '', 'CO': 'P[EN]'}"""

missing = []

page = 0
while True:
    base_url = f"https://www.takaratomy.co.jp/products/en.wixoss/card/itemsearch.php?p={page}"
    print(f"page {page}")

    r = requests.get(base_url, "r")

    items = json.loads(r.content)["items"]
    if len(items) == 0:
        break

    for item in items:
        card_name = item["name"].strip() or " "
        card_no = item["card_no"].strip()  or " "
        #image_url = f"https://www.takaratomy.co.jp/products/en.wixoss/card/thumb/{card_no}.jpg"
        card_type = item["card_type"].strip()  or " "

        print(card_name, card_no)
        item_rarities = item["rarity"].split(",")
        for rarity in item_rarities:
            suffix = rarity_suffix.get(rarity)
            code = card_no
            if suffix and rarity != item_rarities[0]:
                code = code.replace("[EN]", suffix)

            image_url = f"https://www.takaratomy.co.jp/products/en.wixoss/card/thumb/{code}.jpg"

            filename = os.path.join("images", f"{code}.jpg")
            if SAVE_IMAGES and not os.path.exists(filename):
                print(f"Saving {image_url}")
                r = requests.get(image_url)
                time.sleep(0.15)
                if r.status_code != 200:
                    print(f"Error: status code {r.status_code}")
                    missing.append(f"{card_name} ({code})")
                    continue
                image_data = io.BytesIO(r.content)
                img = Image.open(image_data)
                img.save(filename, optimize=True)
            elif not os.path.exists(filename):
                print(f"Checking {image_url}")
                r = requests.get(image_url)
                time.sleep(0.15)
                if r.status_code != 200:
                    print(f"Error: status code {r.status_code}")
                    missing.append(f"{card_name} ({code})")
                    continue
                

            card_dict = {
                "name": card_name,
                "code": code,
                "imageUrl": image_url,
                "type": card_type
            }

            cards[code] = card_dict 

    time.sleep(0.15)
    page += 1
print(len(cards))

print("\nThe following images are missing from the database:")
for m in missing:
    print(m)

header = ["code", "name", "type", "imageUrl"]
to_add = {}
with open('missing.tsv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter="\t")
    next(reader)
    for row in reader:
        to_add[row[0]] = {h:row[i] for i, h in enumerate(header)}

to_add.update(cards)
cards = to_add

def write_file(filename, separator):
    open(filename, 'a').close()
    with open(filename, 'w', encoding="utf-8", newline='') as f:
        f.truncate()
        writer = csv.writer(f, delimiter=separator)
        writer.writerow(header)
        for card in cards.values():
            row = [card[key] for key in header]
            writer.writerow(row)

write_file("cards.csv", ",")
write_file("cards.tsv", "\t")