def square_root(number):
    # Zero yields zero
    # One yields one
    if number <= 1:
        return number
    else:
        x = number
        y = 1
        A = number
        while x > y:
            x = (x + y) / 2
            y = A / x
    return x