# QUESTION 2

# Using exception handling code blocks such as try/ except / else / finally,
# write a program that simulates an ATM machine to withdraw money.
# (NB: the more code blocks the better, but try to use at least two key words e.g. try/except)

# Tasks:
# 1. Prompt user for a pin code
# 2. If the pin code is correct then proceed to the next step, otherwise ask a user to type in a password again.
# You can give a user a maximum of 3 attempts and then exit a program.
# 3. Set account balance to 100.
# 4. Now we need to simulate cash withdrawal
# 5. Accept the withdrawal amount
# 6. Subtract the amount from the account balance and display the remaining balance (NOTE! The balance cannot be
# negative!)
# 7. However, when a user asks to ‘withdraw’ more money than they have on their account, then you need to raise an
# error an exit the program.

# I wrote 2 solutions

# First solution

is_success = False
correct_pin = 1234


def validate_pin(pin):
    correct = pin == correct_pin
    cast_pin = str(pin)
    pin_length = len(cast_pin)
    if not (pin_length == 4):
        raise ValueError("Your pin must be 4 digits long")
    if not correct:
        raise ValueError("Incorrect pin.")


for attemptNo in range(3):
    pin_input = int(input('Please enter your pin. Should be 4 digits: '))
    try:
        validate_pin(pin_input)
        is_success = True
        break
    except ValueError as exc:
        print("Invalid input: %s" % exc)


def validate_amount(amount):
    available_balance = 100
    remaining_balance = available_balance - amount
    if remaining_balance >= 0:
        print(f"You have £{remaining_balance} remaining balance.")

    if amount > available_balance:
        raise ValueError('Please withdraw £100 or less')
    if remaining_balance < 0:
        raise ValueError('Insufficient funds.')


if is_success:
    print("You're balance is £100")
    cash_amount = int(input('Please enter the amount you want to withdraw: '))
    try:
        validate_amount(cash_amount)
        print('Please take your money!')
    except ValueError as exc:
        print('Insufficient funds: %s' % exc)

###########################################
# Second solution


# is_success = False
# correct_pin = 1234
#
#
# def validate_pin(pin):
#     count = 0
#     correct = pin == correct_pin
#     while count < 2:
#         if correct:
#             break
#         count += 1
#         pin = int(input('Try again. Pin should be 4 digits long: '))
#     cast_pin = str(pin)
#     pin_length = len(cast_pin)
#     if not (pin_length == 4):
#         raise ValueError("Your pin must be 4 digits long")
#     if not correct:
#         raise ValueError("Incorrect pin.")
#
#
# def validate_amount(amount):
#     available_balance = 100
#     remaining_balance = available_balance - amount
#     if remaining_balance >= 0:
#         print(f"You have £{remaining_balance} remaining balance.")
#
#     if amount > available_balance:
#         raise ValueError('Not enough funds. Please withdraw £100 or less')
#     if remaining_balance < 0:
#         raise ValueError('Insufficient funds. Try a different amount')
#
#
# try:
#     pin_input = int(input('Please enter your pin. Should be 4 digits: '))
#
#     validate_pin(pin_input)
#
#     cash_amount = int(input('Please enter the amount you want to withdraw: '))
#     validate_amount(cash_amount)
#
#
# except ValueError as exc:
#     print("Invalid input: %s" % exc)
# else:
#     is_success = True
#     print("Thank you for using our services!")
# finally:
#     if is_success:
#         print('Please take your money!')
#     else:
#         print('Could not complete cash withdrawal')
