import requests
import json
import csv
import time
import sys
import os
import io
from PIL import Image

SAVE_IMAGES = False
if "--save-images" in sys.argv:
    SAVE_IMAGES = True

SLEEP_TIME = 0

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
special_rarities = ["UR"]
special_rarity_cards = []

page = 0
while True:
    base_url = f"https://www.takaratomy.co.jp/products/en.wixoss/card/itemsearch.php?p={page}"
    print(f"\n=== page {page} ===\n")

    r = requests.get(base_url, "r")
    time.sleep(SLEEP_TIME)

    items = json.loads(r.content)["items"]
    if len(items) == 0:
        break

    for item in items:
        card_name = item["name"].strip() or " "
        card_no = item["card_no"].strip()  or " "
        card_type = item["card_type"].strip()  or " "

        print(card_name, card_no)
        item_rarities = item["rarity"].split(",")
        for rarity in item_rarities:
            suffix = rarity_suffix.get(rarity)
            code = card_no
            if suffix and rarity != item_rarities[0]:
                code = code.replace("[EN]", suffix)
            if rarity in special_rarities:
                special_rarity_cards.append(code)

            image_url = f"https://www.takaratomy.co.jp/products/en.wixoss/card/thumb/{code}.jpg"

            filename = os.path.join("images", f"{code}.jpg")
            if SAVE_IMAGES and not os.path.exists(filename):
                print(f"Saving {image_url}")
                r = requests.get(image_url)
                time.sleep(SLEEP_TIME)
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
                time.sleep(SLEEP_TIME)
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
    page += 1
print(f"TOTAL: {len(cards)}")

print("\nThe following images are missing from the database:")
for m in missing:
    print(m)

print("\nSpecial rarity cards:")
print(json.dumps(special_rarity_cards))

header = ["code", "name", "type", "imageUrl"]
"""
to_add = {}
with open('missing.tsv', encoding="utf-8", newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter="\t")
    next(reader)
    for row in reader:
        to_add[row[0]] = {h:row[i] for i, h in enumerate(header)}

cards.update(to_add)
"""

def write_file(filename, separator):
    open(filename, 'a').close()
    with open(filename, 'w', encoding="utf-8", newline='') as f:
        f.truncate()
        writer = csv.writer(f, delimiter=separator)
        writer.writerow(header)
        for card in cards.values():
            row = [card[key] for key in header]
            writer.writerow(row)

write_file("cards_database_en.tsv", "\t")