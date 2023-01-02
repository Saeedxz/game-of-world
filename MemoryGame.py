import random
import time
import os


def generate_sequence(difficulty):
    random_list = []
    for number in range(difficulty):
        random_list.append(int(random.randint(1, 101)))
    print(random_list)
    time.sleep(0.7)
    # os.system('clear')    # if I use this command I cant type in the console (input)
    print("\n" * 100)
    return random_list

def get_list_from_user(difficulty):
    user_numbers = []
    print(f"Please insert {difficulty} numbers")
    for i in range(difficulty):
        user_numbers.append(int(input("Enter a number: ")))
    return user_numbers

def is_list_equal(random_list, user_numbers):
    random_list.sort()
    user_numbers.sort()
    if random_list == user_numbers:
        return True
    else:
        return False

def play(difficulty):
    random_list = generate_sequence(difficulty)
    user_numbers = get_list_from_user(difficulty)
    if is_list_equal(random_list, user_numbers):
        print("yes")
        return True
    else:
        print("no")
        return False
