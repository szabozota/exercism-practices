def square(number):
    if 0 < number < 65:
        sqr = 2 ** (number-1)
        return sqr
    else:
        raise ValueError("square must be between 1 and 64")       


def total():
    sum = 0
    for i in range(1,65):
        sum = sum + (2 ** (i-1))
    return sum
