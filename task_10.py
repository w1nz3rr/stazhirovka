import string as str_lib

def count_words(string):
    #Валидация
    if not type(string) is str:
        return None
    #Код функции
    string = string.lower()
    list_words = string.split()
    spec_symbol = str_lib.punctuation
    res = {}
    for word in list_words:
        for sym in word:
            if sym in spec_symbol:
                word = word.replace(sym, '')
        if word == '':
            continue
        if not word in res:
            res[word] = 1
        else:
            res[word] += 1
    return res


print(count_words("A man, a plan, a canal -- Panama"))
print(count_words("Doo bee doo bee doo"))
{'a': 3, 'man': 1, 'plan': 1, 'canal': 1, 'panama': 1} #Мой результат
{"a": 3, "man": 1, "canal": 1, "panama": 1, "plan": 1} #Пример