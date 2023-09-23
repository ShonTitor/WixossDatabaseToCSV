import csv

HEADER = ["code", "name", "type", "imageUrl"]
SEPARATOR = "\t"

def load_file(filename):
    with open(filename, 'r', encoding="utf-8", newline='') as f:
        reader = csv.reader(f, delimiter=SEPARATOR)
        next(reader)
        return {row[0]:row for row in reader}

def write_file(rows, filename):
    open(filename, 'a').close()
    with open(filename, 'w', encoding="utf-8", newline='') as f:
        f.truncate()
        writer = csv.writer(f, delimiter=SEPARATOR)
        writer.writerow(HEADER)
        for row in rows:
            writer.writerow(row)

EN_DATABASE    = load_file("cards_database_en.tsv")
ROTATED_PIECES = load_file("pieces.tsv")
MISSING        = load_file("missing.tsv")

MERGED = EN_DATABASE
MERGED.update(ROTATED_PIECES)
MERGED.update(MISSING)

MERGED = sorted([row for row in MERGED.values()])

write_file(MERGED, "cards.tsv")