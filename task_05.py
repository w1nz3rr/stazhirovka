from datetime import datetime, timedelta


def date_in_future(integer):
    # Валидация
    if not  type(integer) is int:
        return datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    # Код функции
    res = datetime.now() + timedelta(days=integer)
    return res.strftime('%d-%m-%Y %H:%M:%S')


print(date_in_future([]))
print(date_in_future(2))