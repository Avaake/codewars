def normalize(arr, fill_value=None):
    if len(arr) == 0:
        return arr
    length = len(max(arr, key=len))
    for index, value in enumerate(arr):
        if len(value) != length:
            arr[index] = value + [fill_value] * (length - len(value))
    return arr


