import os

BAD_RETURN_CODE = -404
SCORES_FILE_NAME = 'score.txt'


def Screen_cleaner():
    os.system('cls||clear')

def reset_file():
    with open(SCORES_FILE_NAME, 'w') as f:
        f.write("0")