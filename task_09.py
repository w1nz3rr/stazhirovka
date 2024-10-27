def connect_dicts(dict1, dict2):
    #Определяем приоритетный словарь
    if sum(dict1.values()) > sum(dict2.values()):
        main_dict, sec_dict = dict1, dict2
    else:
        main_dict, sec_dict = dict2, dict1


    res_dict = {} #Новый словарь

    #Фильтруем второстепенный
    for key in sec_dict:
        if sec_dict[key] >= 10:
            res_dict[key] = sec_dict[key]
    # Фильтруем приоритетный
    for key in main_dict:
        if main_dict[key] >= 10:
            res_dict[key] = main_dict[key]
    #sort&return
    return dict(sorted(res_dict.items(), key=lambda item: item[1]))



print(connect_dicts({ "a": 2, "b": 12 }, { "c": 11, "e": 5 }))
print(connect_dicts({ "a": 13, "b": 9, "d": 11 }, { "c": 12, "a": 15 }))
print(connect_dicts({ "a": 14, "b": 12 }, { "c": 11, "a": 15 }))