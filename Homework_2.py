from flask import Flask
from functions_for_homeworks import amount_letters_query
from functions_for_homeworks import string_generator
from functions_for_homeworks import all_customers
from functions_for_homeworks import unique_names_count
from functions_for_homeworks import all_unique_names
from functions_for_homeworks import total_profit_query
from functions_for_homeworks import navigation_panel


app = Flask('app')


@app.route('/')
def navigation():
    return navigation_panel()


@app.route('/gen/')
def gen():
    link = navigation_panel() + '<br />' + '<br />' + string_generator(amount_letters_query())
    return link


@app.route('/sorting/')
def sorted_db():
    link = navigation_panel() + '<br />' + '<br />' + all_customers()
    return link


@app.route('/names/')
def amount_unique_names():
    link = navigation_panel() + '<br />' + '<br />' + unique_names_count() + '<br />' + all_unique_names()
    return link


@app.route('/profit/')
def total_profit():
    link = navigation_panel() + '<br />' + '<br />' + total_profit_query()
    return link


if __name__ == '__main__':
    app.run(port=5000, debug=True)
