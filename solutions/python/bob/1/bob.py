def response(hey_bob):
    if len(hey_bob.strip()) == 0:
        return str("Fine. Be that way!")
    elif (hey_bob[-1] == "?") and (hey_bob.isupper() == True):
        return str("Calm down, I know what I'm doing!")
    elif (hey_bob.strip()[-1] == "?") and (hey_bob.find("?") > 0):
        return str("Sure.")
    elif hey_bob.isupper() == True:
        return str("Whoa, chill out!")
    else:
        return str("Whatever.")