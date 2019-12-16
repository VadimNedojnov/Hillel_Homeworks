from flask import Flask
from functions_for_homeworks import amount_letters_query
from functions_for_homeworks import string_generator
from functions_for_homeworks import all_customers
from functions_for_homeworks import unique_names_count
from functions_for_homeworks import all_unique_names


app = Flask('app')


@app.route('/gen')
def gen():
    return string_generator(amount_letters_query())


@app.route('/sorting')
def sorted_db():
    return all_customers()


@app.route('/names')
def amount_unique_names():
    return unique_names_count() + f'<br />{all_unique_names()}'


if __name__ == '__main__':
    app.run(port=5000, debug=True)
