import random
from currency_converter import CurrencyConverter

def get_money_interval(d,t):
    return (t - (5 - d), t + (5 - d))

def get_guess_from_user():
    while True:
        try:
            num = int(input("Please enter your guess: "))
            while num < 0:
                print("Please insert a number greater than 0!")
                num = int(input("Please enter your guess: "))
            return num
        except ValueError:
            print("Please insert a number!")

def play(d):
    currency_rate = (CurrencyConverter().convert(1, 'USD', 'ILS'))
    random_number = random.randint(1, 100)
    t = random_number * currency_rate
    interval = get_money_interval(d,t)
    user_guess = get_guess_from_user()
    return interval[0] <= user_guess <= interval[1]
