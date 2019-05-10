import csv

items = {}

"""
'Cosmetics' : 0,

"""
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

        try:
            items[item_type] += item_profit
        except KeyError:
            items[item_type] = item_profit
    print(items)
#         # List of total profits
#         profit_list = [profit_f, profit_cl, profit_m, profit_be, profit_o, profit_co, profit_s, profit_pc, profit_h,
#                        profit_bf, profit_v, profit_ce]
#         # Choose best profit
#         if max(profit_list) == profit_f:
#             best_item = 'Fruit'
#         elif max(profit_list) == profit_cl:
#             best_item = 'Clothes'
#         elif max(profit_list) == profit_m:
#             best_item = 'Meat'
#         elif max(profit_list) == profit_be:
#             best_item = 'Beverages'
#         elif max(profit_list) == profit_o:
#             best_item = 'Office Supplies'
#         elif max(profit_list) == profit_co:
#             best_item = 'Cosmetics'
#         elif max(profit_list) == profit_s:
#             best_item = 'Snacks'
#         elif max(profit_list) == profit_pc:
#             best_item = 'Personal Care'
#         elif max(profit_list) == profit_h:
#             best_item = 'Household'
#         elif max(profit_list) == profit_bf:
#             best_item = 'Baby Food'
#         elif max(profit_list) == profit_v:
#             best_item = 'Vegetables'
#         elif max(profit_list) == profit_ce:
#             best_item = 'Cereal'
#         # Choose best country
#         if row[2] == best_item and float(row[13]) > country_profit:
#             country_profit = float(row[13])
#             best_country = row[1]
# # Print results
# print("Fruits profit: " + str(profit_f))
# print("Clothes profit: " + str(profit_cl))
# print("Meat profit: " + str(profit_m))
# print("Beverages profit: " + str(profit_be))
# print("Office Supplies profit: " + str(profit_o))
# print("Cosmetics profit: " + str(profit_co))
# print("Snacks profit: " + str(profit_s))
# print("Personal Care profit: " + str(profit_pc))
# print("Household profit: " + str(profit_h))
# print("Baby Food profit: " + str(profit_bf))
# print("Vegetables profit: " + str(profit_v))
# print("Cereal profit: " + str(profit_ce))
# print()
# print("The most profitable item is " + best_item)
# print()
# print("The best country to advertise %s to is %s, with a profit of %d" % (best_item, best_country, country_profit))
# print()
# print("Done")
