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
    else:
        last_digit = num[15]
        rest_of_nums = num[:15]
        reversed_num = reverse(rest_of_nums)
        for index in range(len(reversed_num)):
            reversed_num[index] = int(reversed_num[index])
            if index % 2 == 0:
                reversed_num[index] *= 2
                if reversed_num[index] > 9:
                    reversed_num[index] -= 9
        total = sum(reversed_num)
        if total % 10 != int(last_digit):
            return False
        else:
            return True


with open("Book1.csv") as old_csv:
    with open("MyNewFile.csv", 'w', newline='') as new_csv:
        print("Writing file...   ")
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        for row in reader:
            old_number = row[0]
            if validate(old_number):
                writer.writerow(row)
