def find_outlier(integers):
    even = [num for num in integers[:3] if num % 2 == 0]
    majority_even = len(even) > 1

    if majority_even:
        return next(num for num in integers if num % 2 != 0)
    else:
        return next(num for num in integers if num % 2 == 0)


print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))