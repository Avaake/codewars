def pig_it(text):
    res = []
    for i in text.split():
        if i.isalpha():
            res.append(i[1::] + i[0] + "ay")
        else:
            res.append(i)
    return " ".join(res)