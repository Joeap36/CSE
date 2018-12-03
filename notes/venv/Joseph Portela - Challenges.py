# 1

def challenge1(first_name, last_name):
    return (last_name, first_name)

print(challenge1("Joseph", "Portela"))

# 2

def challenge2(number_1):
    number_list_1 = list(number_1)
    if number_list_1[len(number_list_1) - 1] == (1, 3, 5, 7, 9):
        number_state = "odd"
    elif number_list_1[len(number_list_1) - 1] != (1, 3, 5, 7, 9):
        number_state = "even"
    return number_state

print(challenge2(37))
