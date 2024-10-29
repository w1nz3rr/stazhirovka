import string


def valid_name(data_name):
    if not type(data_name) is str:
        raise ValueError('Название должно быть строкой')
    special_symbol = string.punctuation
    for char in data_name:
        if char in special_symbol:
            raise ValueError('Название не должно содержать спецсимволов')

def valid_calories(data_calories):
    if type(data_calories) is str:
        special_symbol = string.punctuation
        for char in data_calories:
            if char.isalpha() or char in special_symbol:
                raise ValueError('Введите коректное число каллорий')

    if int(data_calories) <= 0:
        raise ValueError('Число каллорий должно быть больше 0')

class Dessert:
    def __init__(self, name='Cake', calories=150):
        valid_name(data_name=name)
        valid_calories(data_calories=calories)
        self.__name = name
        self.__calories = int(calories)

    @property
    def get_name(self):
        return self.__name

    @get_name.setter
    def get_name(self, data):
        valid_name(data_name=data)
        self.__name = data

    @property
    def get_calories(self):
        return self.__calories

    @get_calories.setter
    def get_calories(self, data):
        valid_calories(data_calories=data)
        self.__calories = data

    def is_healthy(self):
        if self.__calories < 200:
            return True
        return False

    def is_delicious(self):
        return True

#тесты
test1 = Dessert()
print(test1.get_name, test1.get_calories)
print(test1.is_healthy())
print(test1.is_delicious())
test1.get_name = 'Бисквит'
test1.get_calories = 300
print(test1.get_name, test1.get_calories)
print(test1.is_healthy())
print(test1.is_delicious())
test2 = Dessert('Конфета', '123')
print(test2.get_name, test2.get_calories)
print(test2.is_healthy())
print(test2.is_delicious())





