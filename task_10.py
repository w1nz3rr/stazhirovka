def count_words(string):
    #Валидация
    if not type(string) is str:
        return None
    #Код функции
    string = string.lower()
    list_words = string.split()
    res = {}
    for word in list_words:
        if word[-1] == ',':
            word = word[:-1]
        if not word in res:
            res[word] = 1
        else:
            res[word] += 1

    return res


print(count_words("A man, a plan, a canal -- Panama"))
print(count_words("Doo bee doo bee doo"))