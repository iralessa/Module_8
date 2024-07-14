# -*- coding: utf-8 -*-
from threading import Thread
from time import sleep
from queue import Queue

print("\033[93m" + '10-ый модуль, "Очереди для обмена данными между потоками"' + "\033[0m")

print("\033[94m" + f'Задача "сеть кафе"' + "\033[0m")

class Table:
    def __init__(self, number, is_busy=False):
        self.number = number
        self.is_busy = is_busy

    def mark_as_busy(self):
        self.is_busy = True

    def mark_as_free(self):
        self.is_busy = False

class Cafe:
    def __init__(self, tables):
        self.tables = tables  # Список столов
        self.queue = Queue()  # Очередь посетителей

    def start_Thread(self):
        # Запускаем поток для прибытия посетителей
        customer_arrival_thread = Thread(target=self.customer_arrival)
        customer_arrival_thread.start()

    def customer_arrival(self):
        for i in range(1, 21):  # приход 20 посетителей
            sleep(1)  # Приход посетителя каждую секунду
            customer = f"Посетитель номер-{i}"  # имя посетителя
            print(f" {customer} прибыл.")
            self.queue.put(customer)  # Посетитель добавляется в очередь
            self.serve_customer(customer)  # Обслуживаем посетителя

    def serve_customer(self, customer):
        served = False
        while not served:
            for table in self.tables:
                if not table.is_busy:
                    table.mark_as_busy()
                    served = True
                    print(f" {customer} сел за стол {table.number}.")
                    customer_thread = Thread(target=self.handle_customer, args=(customer, table))
                    customer_thread.start()


                    break
            if not served:
                print(f"{customer} ожидает свободный стол.")
                sleep(5)

    def handle_customer(self, customer, table):
        sleep(5)  # Время обслуживания 5 секунд
        table.mark_as_free()
        print(f"{customer} покушал и ушёл со стола {table.number}.")


# Создаем столики в кафе
table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

# Инициализируем кафе
cafe = Cafe(tables)

# Запускаем симуляцию прихода посетителей
cafe.start_Thread()