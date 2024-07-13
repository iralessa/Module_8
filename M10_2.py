# -*- coding: utf-8 -*-
from threading import Thread
from time import sleep

print("\033[93m" + f'10-ый модуль,Домашнее задание по теме "Потоки на классах"' + "\033[0m")
print("\033[91m" + f'Задача "За честь и отвагу!"' + "\033[0m")

class Knight(Thread):
    res = []

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = 100 # количество врагов
        self.days_fought = 0 # количество дней битвы
    def run(self):
        print(f"{self.name}, на нас напали!")
        while self.enemies > 0:
            self.days_fought += 1
            print(f"{self.name}, сражается {self.days_fought} день(дня)..., осталось {self.enemies} воинов.")
            sleep(1)  # Задержка на 1 секунду
            self.enemies -= self.power
        print(f"{self.name} одержал победу спустя {self.days_fought} дней(дня)!")

# Создание объектов и запуск потоков
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

first_knight.start()
second_knight.start()

# Ожидание завершения потоков
first_knight.join()
second_knight.join()


print("\033[91m" + f'Все битвы закончились!' + "\033[0m")

