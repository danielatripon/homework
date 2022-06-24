# QUESTION 3

# TASK 3 (Testing)
# Question 1
# Use the Simple ATM program to write unit tests for your functions.
# You are allowed to re-factor your function to ‘untangle’ some logic into smaller
# blocks of code to make it easier to write tests.
# Try to write at least 5 unit tests in total covering various cases.

correct_pin = 1234


def validate_pin1(pin):
    correct = pin == correct_pin
    if correct:
        return pin

    if not correct:
        raise ValueError("Incorrect pin.")


def validate_pin2(pin):
    correct = pin == correct_pin
    if correct:
        return pin
    cast_pin = str(pin)
    pin_length = len(cast_pin)
    if not (pin_length == 4):
        raise ValueError("Your pin must be 4 digits long")


def validate_amount1(amount):
    available_balance = 100
    remaining_balance = available_balance - amount
    if remaining_balance >= 0:
        print(f"You have £{remaining_balance} remaining balance.")

    if amount > available_balance:
        raise ValueError('Not enough funds. Please withdraw £100 or less')


def validate_amount2(amount):
    available_balance = 100
    remaining_balance = available_balance - amount
    if remaining_balance >= 0:
        print(f"You have £{remaining_balance} remaining balance.")

    if remaining_balance < 0:
        raise ValueError('Insufficient funds. Try a different amount')


# validate_pin1(1234)
# validate_pin1(1234)
# validate_pin2(1234)
# validate_amount1(200)
# validate_amount2(110)
