from Live import load_game, welcome

yes_choices = ['yes', 'y']
no_choices = ['no', 'n']

player_name = input("type your name:")

welcome(f"{player_name}")

while True:
    load_game()
    ans = input("do you want to play again (yes/no)?")
    if ans.lower() in yes_choices:
        continue
    elif ans.lower() in no_choices:
        break
    else:
        print('Type yes or no')
        break