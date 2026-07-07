import csv

def read_csv(path):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))

def write_csv(path, rows, fields):
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

def filter_rows(rows, key, value):
    return [r for r in rows if r.get(key) == value]
