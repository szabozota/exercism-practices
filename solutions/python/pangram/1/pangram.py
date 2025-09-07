def is_pangram(sentence):
    lower = sentence.lower()
    res = set()
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for ch in lower:
        if ch in alphabet:
            res.add(ch)
        else:
            continue
    if len(res) == 26:
        return True
    else:
        return False