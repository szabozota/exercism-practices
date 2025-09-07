def is_valid(isbn):
    d = []
    for ch in isbn:
        if (ch == "X") and (ch == isbn[-1]):
            ch = 10
            d.append(ch)
        elif ch == "-":
            continue
        elif ch.isnumeric() == False:
            return False
        else:
            d.append(int(ch))
    if len(d) == 10:
        formula = (d[0] * 10 + d[1] * 9 + d[2] * 8 + d[3] * 7 + d[4] * 6 + d[5] * 5 + d[6] * 4 + d[7] * 3 + d[8] * 2 + d[9] * 1) % 11
        if formula == 0:
            return True
        else:
            return False
    else:
        return False