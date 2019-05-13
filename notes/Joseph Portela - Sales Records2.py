import csv

items = {}

with open("Sales Records.csv") as old_csv:
    reader = csv.reader(old_csv)
    best_item = None
    country_profit = 0
    best_country = None
    for row in reader:
        if row[0] == 'Region':
            continue
        # Add profits
        item_profit = float(row[13])
        item_type = row[2]
        country = row[1]
        try:
            items[item_type]['Total Profit'] += item_profit
        except KeyError:
            items[item_type] = {}
            items[item_type]['Total Profit'] = item_profit
        if items[item_type]['Best Country'] < item_profit:
            try:
                items[item_type]['Best Country'] = country
            except KeyError:
                
print(items)
