import csv


def check_len(num: str):
    if len(num) == 16:
        return True
    return False


def reverse(num: str):
    return list(num[::-1])


def validate(num: str):
    if not check_len(num):
        return False
    last_digit = num[15]
    rest_of_nums = num[:15]
    reversed = reverse(rest_of_nums)
    for index in range(len(reversed)):
        reversed[index] = int(reversed[index])
        if index % 2 == 0:
            index *= 2
            if index > 9:
                index -= 9

    print(reversed)


# print(len("7009235029262260"))
print(validate("7009235029262260"))

# with open("Book1.csv") as old_csv:
#     with open("MyNewFile.csv", 'w', newline='') as new_csv:
#         print("Writing file...   ")
#         reader = csv.reader(old_csv)
#         writer = csv.writer(new_csv)
#         for row in reader:
#             old_number = row[0]  # This is a string
#             if validate(old_number):
#                 writer.writerow(row)
