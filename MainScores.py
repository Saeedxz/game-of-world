from flask import Flask, render_template
from Utils import SCORES_FILE_NAME, BAD_RETURN_CODE


app = Flask(__name__)
@app.route('/')
def score():
    try:
        score = open(SCORES_FILE_NAME, 'r').read()
        return render_template('score.html', SCORE=score)
    except BaseException:
        error = BAD_RETURN_CODE
        return render_template('error.html', ERROR=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0')