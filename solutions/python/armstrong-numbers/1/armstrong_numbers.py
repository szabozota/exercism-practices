def is_armstrong_number(number):
    digit = len(str(number))
    result = 0
    for x in str(number):
        result += int(x) ** digit
    if number == result:
        return True
    else:
        return False