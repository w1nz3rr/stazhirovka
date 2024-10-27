from task_11 import Dessert, valid_name, valid_calories

list_flavor = ['nuts', 'black licorice', 'raspberry', 'chocolate', 'caramel', 'coconut', 'coffee', 'orange']

def valid_flavor(data_flavor):
    if not type(data_flavor) is str:
        raise TypeError("Некоретный ввод вкуса")
    if data_flavor not in list_flavor:
        raise  ValueError("Такого вкуса дисерта не существует")

class JellyBean(Dessert):
    def __init__(self, name='cake', calories=150, flavor='nuts'):
        valid_name(data_name=name)
        valid_calories(data_calories=calories)
        super().__init__(name, calories)
        self.__flavor = flavor

    @property
    def get_flavor(self):
        return self.__flavor

    @get_flavor.setter
    def get_flavor(self, data):
        valid_flavor(data_flavor=data)
        self.__flavor = data

    def is_delicious(self):
        if self.__flavor != "black licorice":
            return True
        return False

test3 = JellyBean()
print(test3.get_name, test3.get_calories, test3.get_flavor)
print(test3.is_delicious())
print(test3.is_healthy())
test3.get_name = 'cake2'
test3.get_calories = 300
test3.get_flavor = 'black licorice'
print(test3.get_name, test3.get_calories, test3.get_flavor)
print(test3.is_delicious())
print(test3.is_healthy())
