import csv

items = {}

with open("Sales Records.csv") as old_csv:
    reader = csv.reader(old_csv)
    best_profit = 0
    best_item = None
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
        try:
            if items[item_type]['Country Profit'] < item_profit:
                items[item_type]['Best Country'] = country
                items[item_type]['Country Profit'] = item_profit
        except KeyError:
            items[item_type]['Country Profit'] = item_profit
            items[item_type]['Best Country'] = country
for product in items.keys():
    print("The total profit from %s is %d, and the best country to advertise this to is %s, with a profit of %d."
          % (product, items[product]['Total Profit'], items[product]['Best Country'],
             items[product]['Country Profit']))
    if items[product]['Total Profit'] > best_profit:
        best_profit = items[product]['Total Profit']
        best_item = product
print()
print("The best product for the company is %s, with a profit of %d." % (best_item, best_profit))
