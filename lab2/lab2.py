# задание 1

# name = str(input())
# def greet(name):
#     print('Привет', name)
# greet(name)
#
# number = int(input())
# def square(number):
#     print(number**2)
# square(number)
#
#
# x = int(input())
# y = int(input())
# def max_of_two(x,y):
#     if x>y:
#         print(x)
#     elif x==y:
#         print('Числа равны')
#     else:
#         print(y)
# max_of_two(x,y)
#
#
# number = int(input())
# def is_prime(number):
#     count = 0
#     for i in range(2,number):
#         if number%i == 0:
#             count += 1
#         if count != 0 :
#             return False
#         else:
#             return True
# print(is_prime(number))
#
name = str(input('Введите имя: '))
age = int(input('Введите возраст: '))


def describe_person(name, age=30):
    return f'Меня зовут {name} мне {age} лет'


print(describe_person(name))
