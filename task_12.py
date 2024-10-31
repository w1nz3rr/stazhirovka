import string
from task_11 import Dessert



# list_flavor = ['nuts', 'black licorice', 'raspberry', 'chocolate', 'caramel', 'coconut', 'coffee', 'orange']

# def valid_flavor(data_flavor):
#     if not type(data_flavor) is str:
#         raise TypeError("Некоретный ввод вкуса")
#     special_symbol = string.punctuation
#     for char in data_flavor:
#         if char in special_symbol:
#             raise ValueError('Вкус не должен содержать спецсимволов')
#     if data_flavor not in list_flavor:
#         raise  ValueError("Такого вкуса дисерта не существует")

class JellyBean(Dessert):
    def __init__(self, name='cake', calories=150, flavor='nuts'):
        # valid_name(data_name=name)
        # valid_calories(data_calories=calories)
        super().__init__(name, calories)
        self.__flavor = flavor

    @property
    def flavor(self):
        return self.__flavor

    @flavor.setter
    def flavor(self, data):
        # valid_flavor(data_flavor=data)
        self.__flavor = data

    def is_delicious(self):
        if self.__flavor != "black licorice":
            return True
        return False

dessert = JellyBean()
if not issubclass(dessert.__class__, JellyBean): raise Exception("Invalid inheritance")
dessert.name = "test_name"
print(dessert.name)
dessert.name = "test_name2"
print(dessert.name)
if dessert.name != "test_name2": raise Exception("Setter for name is not working")
dessert.calories = "test_calories"
print(dessert.calories)
dessert.calories = "test_calories2"
print(dessert.calories)
if dessert.calories != "test_calories2": raise Exception("Setter for calories is not working")
print(dessert.is_delicious())
if not dessert.is_delicious(): raise Exception("Invalid method result")
dessert.flavor = "test_flavor"
print(dessert.flavor)
print(dessert.is_healthy())
dessert.calories = 300
print(dessert.calories)
print(dessert.is_healthy())
