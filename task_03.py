def max_odd(array):
    new_array = []
    for el in array:
        if type(el) is int or type(el) is float:
            new_array.append(int(el))

    if len(new_array) == 0:
        return None

    new_array2 = []
    for item in new_array:
        if item % 2 == 1:
            new_array2.append(item)

    if len(new_array2) == 0:
        return None

    return max(new_array2)


print(max_odd([1, 2, 3, 4, 4]))
print(max_odd([21.0, 2, 3, 4, 4]))
print(max_odd(['ololo', 2, 3, 4, [1, 2], None]))
print(max_odd(['ololo', 'fufufu']))
print(max_odd([2, 2, 4]))
