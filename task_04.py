def sort_list(lst):
    # Валидация
    if len(lst) == 0:
        return []
    if not type(lst) is list:
        return f'{lst} не является массовом'
    # Код функции
    min_el = min(lst)
    max_el = max(lst)
    count_index = 0
    for el in lst:

        if el == min_el:
            lst[count_index] = max_el
            count_index += 1
            continue

        if el == max_el:
            lst[count_index] = min_el
        count_index += 1
    res = lst
    res.append(min_el)
    return res


print(sort_list([]) )
print(sort_list([2, 4, 6, 8]))
print(sort_list([1]))
print(sort_list([1, 2, 1, 3]))