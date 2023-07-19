import random
import sys


def check_length(user_input):
    if user_input.isdigit() and (len(user_input) >= 1 and len(user_input) <= 3):
        return int(user_input)

    print("Invalid input.")
    sys.exit()


def check_choice(user_input):
    if user_input.isdigit() and len(user_input) == 1:
        if user_input >= "1" and user_input <= "3":
            return int(user_input)

    print("Invalid input.")
    sys.exit()


def generate_random_password(length, choice):
    random_list = []
    password = ""
    for i in range(0, length):
        random_number_big_alpha = random.randint(65, 90)
        random_list.append(random_number_big_alpha)
        random_element_small_alpha = random.randint(97, 122)
        random_list.append(random_element_small_alpha)
        if choice == 2 or choice == 3:
            random_element_numeric = random.randint(48, 57)
            random_list.append(random_element_numeric)
        if choice == 3:
            random_element_special_char = random.randint(33, 47)
            random_list.append(random_element_special_char)
        random_element = random.choice(random_list)
        password = password + chr(random_element)
    print("              ")
    print("Password: ", password)
    print("              ")
    return password


try:
    num_args = len(sys.argv) - 1
    if num_args != 2:
        raise ValueError("Invalid input format")

    length = str(sys.argv[1])
    length = check_length(length)
    choice = str(sys.argv[2])
    choice = check_choice(choice)
    generate_random_password(length, choice)

except ValueError as e:
    print(str(e))
    sys.exit()
