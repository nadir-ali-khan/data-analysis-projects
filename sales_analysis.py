# v45597
import csv
from collections import defaultdict

def summarize(path):
    totals = defaultdict(float)
    with open(path) as f:
        for row in csv.DictReader(f):
            totals[row["category"]] += float(row.get("amount", 0))
    return dict(totals)

def top_n(totals, n=5):
    return sorted(totals.items(), key=lambda x: x[1], reverse=True)[:n]
