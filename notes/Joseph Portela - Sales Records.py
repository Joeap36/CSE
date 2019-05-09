import csv

with open("Sales Records.csv") as old_csv:
    reader = csv.reader(old_csv)
    profit_f = 0
    profit_cl = 0
    profit_m = 0
    profit_be = 0
    profit_o = 0
    profit_co = 0
    profit_s = 0
    profit_pc = 0
    profit_h = 0
    profit_bf = 0
    profit_v = 0
    profit_ce = 0
    for row in reader:
        if row[2] == 'Fruits':
            profit_f += float(row[13])
        elif row[2] == 'Clothes':
            profit_cl += float(row[13])
        elif row[2] == 'Meat':
            profit_m += float(row[13])
        elif row[2] == 'Beverages':
            profit_be += float(row[13])
        elif row[2] == 'Office Supplies':
            profit_o += float(row[13])
        elif row[2] == 'Cosmetics':
            profit_co += float(row[13])
        elif row[2] == 'Snacks':
            profit_s += float(row[13])
        elif row[2] == 'Personal Care':
            profit_pc += float(row[13])
        elif row[2] == 'Household':
            profit_h += float(row[13])
        elif row[2] == 'Baby Food':
            profit_bf += float(row[13])
        elif row[2] == 'Vegetables':
            profit_v += float(row[13])
        elif row[2] == 'Cereal':
            profit_ce += float(row[13])
profit_list = [profit_f, profit_cl, profit_m, profit_be, profit_o, profit_co, profit_s, profit_pc, profit_h, profit_bf,
               profit_v, profit_ce]
if max(profit_list) == profit_f:
    best_item = 'Fruit'
elif max(profit_list) == profit_cl:
    best_item = 'Clothes'
elif max(profit_list) == profit_m:
    best_item = 'Meat'
elif max(profit_list) == profit_be:
    best_item = 'Beverages'
elif max(profit_list) == profit_o:
    best_item = 'Office Supplies'
elif max(profit_list) == profit_co:
    best_item = 'Cosmetics'
elif max(profit_list) == profit_s:
    best_item = 'Snacks'
elif max(profit_list) == profit_pc:
    best_item = 'Personal Care'
elif max(profit_list) == profit_h:
    best_item = 'Household'
elif max(profit_list) == profit_bf:
    best_item = 'Baby Food'
elif max(profit_list) == profit_v:
    best_item = 'Vegetables'
elif max(profit_list) == profit_ce:
    best_item = 'Cereal'
print("Fruits profit: " + str(profit_f))
print("Clothes profit: " + str(profit_cl))
print("Meat profit: " + str(profit_m))
print("Beverages profit: " + str(profit_be))
print("Office Supplies profit: " + str(profit_o))
print("Cosmetics profit: " + str(profit_co))
print("Snacks profit: " + str(profit_s))
print("Personal Care profit: " + str(profit_pc))
print("Household profit: " + str(profit_h))
print("Baby Food profit: " + str(profit_bf))
print("Vegetables profit: " + str(profit_v))
print("Cereal profit: " + str(profit_ce))
print()
print("The most profitable item is " + best_item)
print()
print("Done")
