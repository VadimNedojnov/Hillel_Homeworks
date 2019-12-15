import string
import random
from validation import empty_parameter_validation
from validation import parameter_isdigit_validation
from validation import max_symbols_amount_validation


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
