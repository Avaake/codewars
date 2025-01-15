def maskify(cc):
    if len(cc) <= 4 or cc == "":
        return cc
    return "#" * len(cc[:-4]) + cc[-4:]
