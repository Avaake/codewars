def alphabet_position(text):
    from string import ascii_lowercase
    alphabet: list[str] = list(ascii_lowercase)
    return " ".join(str(alphabet.index(i) + 1) for i in text.lower() if i in alphabet)