def multiply_numbers(*args):
    #Код функции
    args = str(args)
    count = 0
    temp_el = 1

    for el in list(args):

        if el.isdigit():
            temp_el *= int(el)
            count += 1

    if count < 2:
        return None

    return temp_el



print(multiply_numbers())
print(multiply_numbers('ss'))
print(multiply_numbers('1234'))
print(multiply_numbers('sssdd34'))
print(multiply_numbers(2.3))
print(multiply_numbers([5, 6, 4]))