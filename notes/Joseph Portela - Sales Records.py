import csv

with open("Sales Records.csv") as old_csv:
    reader = csv.reader(old_csv)
    highest_profit = 0
    for row in reader:
        if row[2] == 'Fruits':
            current_profit = float(row[13])
            if current_profit > highest_profit:
                highest_profit = current_profit
print(highest_profit)
print("Done")
