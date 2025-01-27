def to_underscore(strng: str) -> str:
    result = []
    if not isinstance(strng, str):
        return str(strng)
    for char in strng:
        if char.isupper() and result:
            result.append("_")
        result.append(char.lower())
    return "".join(result)
