# zadanie 1

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def get_info(self):
        return f"Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}"

book = Book('Гарри Поттер', 'Джоан Роулинг', '1997')

print(book.get_info())

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def get_radius(self):
#         return f'Радиус равен {self.radius}'
#
#     def set_radius(self, new_radius):
#         self.radius = new_radius
#
# obj = Circle('5')
# obj.set_radius('8')
#
# print(obj.get_radius())
