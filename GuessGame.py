import random
from Score import add_score


def generate_number(difficulty):
    random_number = int(random.randint(1, difficulty))
    return random_number

def get_guess_from_user(difficulty):
    print(f"You need to guess a number between 1 to {difficulty}: ")
    input_number = int(input())
    return input_number

def compare_results(random_number, input_number):
    if random_number == input_number:
        return True
    else:
        return False

def play(difficulty):
    random_number = generate_number(difficulty)
    input_number = get_guess_from_user(difficulty)
    if compare_results(random_number, input_number) == True:
        print("you won")
        add_score(difficulty)
        return True
    else:
        print("you lost")
        return False
