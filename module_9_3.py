class EvenNumbers:
    def __init__(self, start=0, end=1):
        self.start = start
        self.end = end
        self.i = 0
        self.k = 0

    def __iter__(self):
        self.i = self.start
        return self

    def __next__(self):
        if self.i < self.end:

            if self.i % 2 == 0:
                self.k += 1
                result = self.i
                self.i += 2  # переходим к следующему чётному числу
                return result
            else:
                self.i += 1  # переходим к следующему числу
        raise StopIteration


# Пример использования исправленного класса EvenNumbers
en = EvenNumbers(10, 25)
for n in en:
    print(n)
if StopIteration:
    print('\033[93m' + 'Перебор закончен! Кол-во выведеных значений = ',str(en.k) + '\033[0m')