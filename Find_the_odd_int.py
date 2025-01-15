def find_it(seq):
    from collections import Counter
    return int("".join(str(k) for k, v in Counter(seq).items() if v % 2 != 0))