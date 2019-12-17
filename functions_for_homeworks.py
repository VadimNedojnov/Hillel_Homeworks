import string
import random
import sqlite3
import os
from validation import empty_parameter_validation
from validation import parameter_isdigit_validation
from validation import max_symbols_amount_validation


# ----------------------------------------------------------------- For second homework, start

def navigation_panel_link(key):
    return f'<a href="http://127.0.0.1:5000/{key}">{key}</a>'


def navigation_panel_link_2(key):
    return f'<a href="http://127.0.0.1:5000/{key}?amount=50">{key}</a>'


def navigation_panel():
    panel = f'{navigation_panel_link("")} {navigation_panel_link_2("gen")} {navigation_panel_link("sorting")} ' \
            f'{navigation_panel_link("names")} {navigation_panel_link("profit")}'
    return panel


def amount_letters_query():
    first_validation = empty_parameter_validation()
    print(first_validation)
    if first_validation != "Error exception: The value is empty.":
        second_validation = parameter_isdigit_validation(first_validation)
        if second_validation != "Error exception: Incorrect value. The value must be integer.":
            return max_symbols_amount_validation(second_validation)
        else:
            return second_validation
    else:
        return first_validation


def string_generator(amount):
    if amount.isdigit():
        ready_string = ''.join(random.choice(string.ascii_letters) for i in range(int(amount)))
        return ready_string
    else:
        return amount


def exec_query(query):
    database_path = os.path.join(os.getcwd(), 'chinook.db')
    conn = sqlite3.connect(database_path)
    cur = conn.cursor()
    cur.execute(query)
    record = cur.fetchall()
    return str(record)


def all_customers():
    query = f'SELECT * FROM customers ORDER BY State, City;'
    first_result = exec_query(query)
    final_result = '<br />'.join(first_result.split('), ('))
    return final_result[2:-2]


def unique_names_count():
    query = f'SELECT COUNT(DISTINCT FirstName) FROM customers;'
    result = exec_query(query)
    return f'Amount of unique names in DB: {result[2:-3]}'


def all_unique_names():
    query = f'SELECT DISTINCT FirstName FROM customers;'
    first_result = exec_query(query)
    result = '<br />'.join(first_result.split('), ('))
    return result[2:-3]


def total_profit_query():
    query = f'SELECT SUM(UnitPrice * Quantity) FROM invoice_items;'
    result = exec_query(query)
    return f'Total profit: {result[2:-3]}'

# ----------------------------------------------------------------- For second homework, end




