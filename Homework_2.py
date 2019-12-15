from flask import Flask
from functions_for_homeworks import amount_letters_query
from functions_for_homeworks import string_generator
import os


app = Flask('app')


@app.route('/gen')
def gen():
    return string_generator(amount_letters_query())


if __name__ == '__main__':
    app.run(port=5000, debug=True)
