# 1

def challenge1(first_name, last_name):
    return (last_name, first_name)

print(challenge1("Joseph", "Portela"))

# 2
"""
def challenge2(number_1):
    number_list_1 = list(number_1)
    if number_list_1[len(number_list_1) - 1] == (1, 3, 5, 7, 9):
        number_state = "odd"
    elif number_list_1[len(number_list_1) - 1] != (1, 3, 5, 7, 9):
        number_state = "even"
    
    return number_state

print(challenge2(37))
"""
# 3

def challenge3(base1, height1):
    return (base1*height1)/2

print(challenge3(9, 8))

# 4

def challenge4(number_2):
    if number_2 > 0:
        number_sign = "positive"
    elif number_2 < 0:
        number_sign = "negative"
    elif number_2 == 0:
        number_sign = "zero"

    return number_sign

print(challenge4(-9))

# 5

def challenge5(radius):
    return (radius**2)*3.14159265358979323846

print(challenge5(3))

# 6

def challenge6(radius2):
    return (radius2**3)*(4/3)*3.14159265358979323846

print(challenge6(7))
