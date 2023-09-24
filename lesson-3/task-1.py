import math
# Геометрические фигуры: абстрактный класс
# Контекст
# Предположим, что мы хотим написать программу для исследования геометрических фигур. Для того
# чтобы это сделать мы решили начать с создания абстрактного класса - “Фигура”.
# ● Задача
# Реализовать класс Shape, содержащий пустые методы get_area и get_perimeter. Использовать библиотеку
# абстрактных классов “ABC” в данном случае - не обязательно.
# ● Решение:

class Shape:
    def get_perimetr(self):
        pass

    def get_area(self):
        pass

# Контекст
# Теперь, когда у вас есть абстрактный класс Shape, ваша следующая задача - получить класс Circle.

# Задача
# Реализовать дочерний от Shape класс Circle, включая следующие работающие методы:
# конструктор класса __init__ - метод инициализации класса Circle.
# get_area - метод для расчета площади круга
# get_perimeter - метод для расчета периметра окружности

class Circle(Shape):
    def __init__ (self, r):
        self.r = r
    def get_perimetr(self):
        return 2*math.pi*self.r
    def get_area(self):
        return math.pi*self.r**2
    
circle_one = Circle(5)
print(circle_one.get_perimetr())
print(circle_one.get_area())

# Контекст
# И наконец, последняя задача - по аналогии с кругом создать класс для треугольника и расчета его характеристик.

# Задача
# Реализовать дочерний от Shape класс Triangle, включая следующие работающие методы:
# конструктор класса __init__ - метод инициализации класса.
# get_area - метод для расчета площади
# get_perimeter - метод для расчета периметра

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def get_perimetr(self):
        return self.a + self.b +self.c
    
    def get_area(self):
        p = self.get_perimetr()/2
        return math.sqrt(p*(p - self.a)*(p - self.b)*(p - self.c))
    
triangle_one = Triangle(3,4,5)
print(triangle_one.get_perimetr())
print(triangle_one.get_area())