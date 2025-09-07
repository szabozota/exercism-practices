def translate(text):
    result = ""
    if text.find(" ") >= 1:
        text = text.split()
        for txt in text:
            if (txt.startswith(("a", "e", "i", "o", "u")) == False) and (txt.find("y") == 2):
                result = result + txt[2:len(txt)] + txt[0:2] + "ay" + " "
            elif (txt.startswith(("a", "e", "i", "o", "u")) == False) and (txt.find("y") == 1):
                result = result + txt[1:len(txt)] + txt[0] + "ay" + " "
            elif (txt.startswith(("a", "e", "i", "o", "u")) == False) and (txt.find("qu") == 2):
                result = result + txt[1:len(txt)] + txt[0] + "ay" + " "
            elif (txt.startswith(("a", "e", "i", "o", "u")) == False) and (txt.find("qu") >= 1):
                result = result + txt[(txt.find("qu")+2):len(txt)] + txt[0] + "qu" + "ay" + " "
            elif (txt.startswith(("a", "e", "i", "o", "u")) == False) and (txt.find("qu") >= 0):
                result = result + txt[(txt.find("qu")+2):len(txt)] + "qu" + "ay" + " "
            elif txt.startswith(("a", "e", "i", "o", "u", "xr", "yt")) == True:
                result = result + txt + "ay" + " "
            elif txt.startswith(("a", "e", "i", "o", "u"), 1, 20) == True:
                result = result + txt[1:len(txt)] + txt[0] + "ay" + " "
            elif txt.startswith(("a", "e", "i", "o", "u"), 2, 20) == True:
                result = result + txt[2:len(txt)] + txt[0:2] + "ay" + " "
            elif txt.startswith(("a", "e", "i", "o", "u"), 3, 20) == True:
                result = result + txt[3:len(txt)] + txt[0:3] + "ay" + " "
        result = result[0:(len(result)-1)]
    elif text.find(" ") == -1:
        if (text.startswith(("a", "e", "i", "o", "u")) == False) and (text.find("y") == 2):
            result = result + text[2:len(text)] + text[0:2] + "ay"
        elif (text.startswith(("a", "e", "i", "o", "u")) == False) and (text.find("y") == 1):
            result = result + text[1:len(text)] + text[0] + "ay"
        elif (text.startswith(("a", "e", "i", "o", "u")) == False) and (text.find("qu") == 2):
            result = result + text[1:len(text)] + text[0] + "ay"
        elif (text.startswith(("a", "e", "i", "o", "u")) == False) and (text.find("qu") >= 1):
            result = result + text[(text.find("qu")+2):len(text)] + text[0] + "qu" + "ay"
        elif (text.startswith(("a", "e", "i", "o", "u")) == False) and (text.find("qu") >= 0):
            result = result + text[(text.find("qu")+2):len(text)] + "qu" + "ay"
        elif text.startswith(("a", "e", "i", "o", "u", "xr", "yt")) == True:
            result = result + text + "ay"
        elif text.startswith(("a", "e", "i", "o", "u"), 1, 20) == True:
            result = result + text[1:len(text)] + text[0] + "ay"
        elif text.startswith(("a", "e", "i", "o", "u"), 2, 20) == True:
            result = result + text[2:len(text)] + text[0:2] + "ay"
        elif text.startswith(("a", "e", "i", "o", "u"), 3, 20) == True:
            result = result + text[3:len(text)] + text[0:3] + "ay"
    return result