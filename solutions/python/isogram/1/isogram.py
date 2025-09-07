def is_isogram(string):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    buffer = set()
    for ch in string.lower():
        if ch in alphabet:
            if ch in buffer:
                return False
            else:
                buffer.add(ch)
        else:
            continue
    return True