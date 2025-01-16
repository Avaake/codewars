def multiply_all(arr):
    def multiply_by(multiplier):
        return list(map(lambda x: x * multiplier, arr))
    return multiply_by
