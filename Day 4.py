lower_limit = 359282
upper_limit = 820401


def check_password(password):
    # It is a six-digit number
    if len(str(password)) != 6:
        return False

    # The value is within the range given in your puzzle input
    if not (lower_limit < password < upper_limit):
        return False

    # Two adjacent digits are the same
    same_digit = []
    last_digit = -1
    last_last_digit = -2
    for digit in str(password):
        if digit == last_digit:
            same_digit.append(digit)
        if last_digit == last_last_digit and digit == last_digit:
            same_digit = [x for x in same_digit if x != digit]
        last_last_digit = last_digit
        last_digit = digit

    if len(same_digit) == 0:
        return False

    # Going from left to right, the digits never decrease
    last_digit = 0
    for digit in str(password):
        if int(digit) < int(last_digit):
            return False
        last_digit = digit

    return True


valid_passwords = []

for possible_password in range(lower_limit, upper_limit, 1):
    if check_password(possible_password):
        valid_passwords.append(possible_password)

print(str(len(valid_passwords)))
