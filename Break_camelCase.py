from string import ascii_uppercase
def solution(s):
    result = s
    for char in ascii_uppercase:
        result = result.replace(char, f" {char}")
    return result
