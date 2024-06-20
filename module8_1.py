def add_everything_up(a, b):
    try:
        if isinstance(a, (int, float, str)) and isinstance(b, (int, float, str)):
            return a + b


    except TypeError:
        return str(a) + str(b)

# Примеры использования функции
print(add_everything_up(123.456, 'строка'))    # Вывод: 123.456строка
print(add_everything_up('яблоко', 4215))       # Вывод: яблоко4215
print(f"{add_everything_up(123.456, 7):.3f}")  # Вывод: 130.456