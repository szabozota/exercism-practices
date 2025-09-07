def is_paired(input_string):
    stack = []
    openers = ["(", "[", "{"]
    closers = [")", "]", "}"]
    pairs = {")": "(", "]": "[", "}": "{"}
    for ch in input_string:
        if ch in openers:
            stack.append(ch)
        elif ch in closers:
            if not stack:
                return False
            else:
                last_open = stack.pop()
                if last_open != pairs[ch]:
                    return False
    return not stack