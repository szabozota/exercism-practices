def convert(number):
    result = str()
    if number % 3 == 0:
        result += str("Pling")
        if number % 5 == 0:
            result += str("Plang")
            if number % 7 == 0:
                result += ("Plong")
            return result
        if number % 7 == 0:
            result += ("Plong")
        return result
    elif number % 5 == 0:
        result += str("Plang")
        if number % 7 == 0:
            result += ("Plong")
        return result
    elif number % 7 == 0:
        result += ("Plong")
        return result
    else:
        return str(number)