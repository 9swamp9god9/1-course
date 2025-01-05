# 1
# class UserAccount:
#
#     def __init__(self, username, email, password):
#         self.username = username
#         self.email = email
#         self.__password = password
#
#
#     def set_password(self, new_password):
#         self.__password = new_password
#
#     def change_password(self, password):
#         if self.__password == password:
#             return True
#         else:
#             return False
#
# obj = UserAccount('romchik', 'rr3rqw@gmail.com', 'chikchik121212')
# obj.set_password('2332')
# print(obj.change_password('212'))
# print(obj.change_password('2332'))
# print(obj)

# 2
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_info(self):
        return f'Марка автомобиля: {self.make}, Модель автомобиля: {self.model}'


car1 = Vehicle('Porsche', '911')
print(car1.get_info())


class Car(Vehicle):
    def __init__(self, make, model, fuel):
        super().__init__(make, model)
        self.fuel = fuel

    def get_info(self):
        base_info = super().get_info()
        return f'{base_info}, Тип топлива: {self.fuel}'


car2 = Car('Porsche', '911', 'бензин')
print(car2.get_info())
