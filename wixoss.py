import requests
import json
import csv
import time

cards = {}

page = 0
while True:
    base_url = f"https://www.takaratomy.co.jp/products/en.wixoss/card/itemsearch.php?p={page}"

    r = requests.get(base_url, "r")

    items = json.loads(r.content)["items"]
    if len(items) == 0:
        print(len(items))
        break

    for item in items:
        card_name = item["name"]
        card_no = item["card_no"]
        image_url = f"https://www.takaratomy.co.jp/products/en.wixoss/card/thumb/{card_no}.jpg"
        card_type = item["card_type"]

        print(card_name, card_no)

        card_dict = {
            "name": card_name,
            "code": card_no,
            "imageUrl": image_url,
            "type": card_type
        }

        cards[card_no] = card_dict 
    time.sleep(0.1)
    page += 1

print(len(cards))

open('cards.csv', 'a').close()
with open('cards.csv', 'w', encoding="utf-8", newline='') as f:
    f.truncate()
    writer = csv.writer(f)
    header = ["code", "name", "type", "imageUrl"]
    writer.writerow(header)
    for card in cards.values():
        row = [card[key] for key in header]
        writer.writerow(row)