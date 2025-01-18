from string import ascii_uppercase, ascii_lowercase, digits
def password(st):
    if len(st) < 8:
        return False
    has_uppercase = any(i for i in ascii_uppercase if i in st)
    has_lowercase = any(i for i in ascii_lowercase if i in st)
    has_digit = any(i for i in digits if i in st)
    return has_uppercase and has_lowercase and has_digit