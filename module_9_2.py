#задача 1
print('\033[91m' + 'Задача 1' + '\033[0m')
def create_function(operation):
    if operation == "add":
        def add(x, y):
            return x + y
        return add
    elif operation == "subtract":
        def subtract(x, y):
            return x - y
        return subtract
    elif operation == "multiply":
        def multiply(x, y):
            return x * y
        return multiply
    elif operation == "divide":
        def divide(x, y):
            if y != 0:
                return x // y
            else:
                raise ZeroDivisionError("Деление на ноль невозможно!!!")
        return divide

# Примеры использования

my_func_add = create_function("add")
print("Сложение =", my_func_add(1, 2))  # Выводит Сложение = 3

my_func_subtract = create_function("subtract")
print("Вычитание =", my_func_subtract(7, 3))  # Выводит Вычитание = 4

my_func_multiply = create_function("multiply")
print("Умножение =", my_func_multiply(5, 1))  # Выводит Умножение = 5

my_func_divide = create_function("divide")
print("Деление =", my_func_divide(12, 2))  # Выводит Деление = 6

try:
    print("Деление =", my_func_divide(7, 0))  # Вызовет исключение ZeroDivisionError
except ZeroDivisionError as e:
    print(e)  # Выводит Деление на ноль невозможно!!!

print('\033[91m' + 'Задача 2' + '\033[0m')
square_lambda = lambda x: x ** 2
def square_1(x):
    return x ** 2
print("Квадрат числа через lambda =",square_lambda(12))
print("Квадрат числа через функцию =",square_1(12))

print('\033[91m' + 'Задача 3' + '\033[0m')

class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        return self.a * self.b

# Пример использования класса Rect
rectangle = Rect(5, 10)
area = rectangle()  # Вызываем объект как функцию, чтобы получить площадь
print("Площадь прямоугольника:", area)