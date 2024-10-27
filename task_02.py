def coincidence(*args):
    # Валидация
    if len(args) != 2:
        return []
    if not type(args[0]) is list:
        return []
    if not type(args[1]) is range:
        return []
    # Код функции
    new_list = []
    for el in args[0]:
        new_el = el
        if type(new_el) is float:
            new_el = int(new_el)
        if new_el in args[1]:
            new_list.append(el)
    return new_list


print(coincidence([1, 2, 3, 4, 5], range(3, 6)))
print(coincidence())
print(coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4)))