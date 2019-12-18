from flask import request


def empty_parameter_validation():
    try:
        return request.args["amount"]
    except:
        return "Error exception: The value is empty."


def parameter_isdigit_validation(amount):
    if amount.isdigit():
        return amount
    else:
        return "Error exception: Incorrect value. The value must be integer."


def max_symbols_amount_validation(amount):
    if int(amount) <= 2000000:
        return amount
    else:
        return "Error exception: Value is over the limit. The limit is 2 000 000 symbols"
