from Live import load_game, welcome
from Utils import Screen_cleaner, reset_file
yes_choices = ['yes', 'y']
no_choices = ['no', 'n']

player_name = input("type your name:")

Screen_cleaner()
welcome(f"{player_name}")

while True:
    load_game()
    ans = input("do you want to play again (yes/no)?")
    if ans.lower() in yes_choices:
        Screen_cleaner()
        continue
    elif ans.lower() in no_choices:
        reset_file()
        break
    else:
        print('Type yes or no')
        reset_file()
        break