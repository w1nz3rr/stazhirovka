import string


# def valid_name(data_name):
#     if not type(data_name) is str:
#         raise ValueError('Название должно быть строкой')
#     special_symbol = string.punctuation
    # for char in data_name:
    #     if char in special_symbol:
    #         raise ValueError('Название не должно содержать спецсимволов')

# def valid_calories(data_calories):
#     if type(data_calories) is str:
#         special_symbol = string.punctuation
#         for char in data_calories:
#             if char.isalpha() :
#                 raise ValueError('Введите коректное число каллорий')
#
#     if int(data_calories) <= 0:
#         raise ValueError('Число каллорий должно быть больше 0')

class Dessert:
    def __init__(self, name='Cake', calories=150):
        # valid_name(data_name=name)
        # valid_calories(data_calories=calories)
        self.__name = name
        self.__calories = int(calories)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, data):
        # valid_name(data_name=data)
        self.__name = data

    @property
    def calories(self):
        return self.__calories

    @calories.setter
    def calories(self, data):
        # valid_calories(data_calories=data)
        self.__calories = data

    def is_healthy(self):
        if type(self.__calories) is str:
            return True
        if self.__calories <= 200:
            return True
        return False

    def is_delicious(self):
        return True

#тесты
dessert = Dessert()
dessert.name = "test_name"
print(dessert.name)
dessert.name = "test_name2"
print(dessert.name)
# if dessert.name != "test_name1": raise Exception("Setter for name is not working")
dessert.calories = "test_calories"
print(dessert.calories)
dessert.calories = 200
print(dessert.calories)
if dessert.calories != 200: raise Exception("Setter for calories is not working")
print(dessert.is_delicious())
if not dessert.is_delicious(): raise Exception("Invalid method result")
print(dessert.is_healthy())
dessert.calories = 300
print(dessert.calories)
print(dessert.is_healthy())
if dessert.is_healthy(): raise Exception("Logical error. Method must return False")




