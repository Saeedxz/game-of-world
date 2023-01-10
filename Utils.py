import os

yes_choices = ['yes', 'y']
no_choices = ['no', 'n']

BAD_RETURN_CODE = 400

def score_file_name(file_name):
    file_name = "Scores.txt"
    Q = input("do you want to change the name of the file (default: 'Scores.txt')?")
    if Q.lower() in yes_choices:
        file_name = input("new file name: ")
        print(f'file name is {file_name}')
    elif Q.lower() in no_choices:
        print('file name is Scores.txt')
    else:
        print('invalid input! file name is Scores.txt')
    with open(f"{file_name}","w+") as my_file:
        my_file.write("0")

def Screen_cleaner():
    os.system('cls||clear')
