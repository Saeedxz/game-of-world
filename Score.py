import os
from Utils import SCORES_FILE_NAME, BAD_RETURN_CODE


def score():
    exists = os.path.isfile(SCORES_FILE_NAME)

    if exists:
        with open(SCORES_FILE_NAME, 'r') as f:
            return f.read()
    else:
        return BAD_RETURN_CODE


def add_score(difficulty):
    points_of_winning = (difficulty * 3) + 5
    
    current_score = int(score())

    if current_score == BAD_RETURN_CODE:
        with open(SCORES_FILE_NAME, 'w') as f:
            f.write(str(points_of_winning))
    else:
        with open(SCORES_FILE_NAME, 'w') as f:
            f.write(str(points_of_winning + current_score))