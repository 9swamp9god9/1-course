# zadanie 1
def read_file(type : int, num_line = 0):
    with open('/Users/swampgod/Desktop/example.txt', 'r', encoding='utf-8') as file:
        if type == 1:
            content = file.read()
            return content
        elif type == 2:
            lst = list()
            for line in file:
                lst.append(line.rstrip())
            return lst[num_line - 1]
        else:
            return 'Укажите действительный тип вывода'

print(read_file(2,1))

#zadanie 2

 def new_file(text: str):
     with open('/Users/swampgod/Desktop/user_input.txt', 'a+', encoding="utf-8") as file:
         file.write(text)
     return print("Данные записаны")


 new_file('AaaaAAAAaaaa')


#zadanie 3

# def read_file(filename: str, type: int, num_line = 0):
#     try:
#         with open(filename, 'r', encoding='utf-8') as file:
#             if type == 1:
#                 content = file.read()
#                 return content
#             elif type == 2:
#                 lst = list()
#                 for line in file:
#                     lst.append(line.rstrip())
#                 return lst[num_line-1]
#             else:
#                 return 'Укажите действительный тип вывода'
#     except FileNotFoundError:
#         return "Вы указали несуществующий файл"
#
# print(read_file('/Users/swampgod/Desktop/example.txt',2,4))
