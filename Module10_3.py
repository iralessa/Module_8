# -*- coding: utf-8 -*-
from threading import Thread,Lock
from time import sleep

print("\033[93m" + '10-ый модуль, "Блокировки и обработка ошибок"' + "\033[0m")

print("\033[94m" + f'Задача "банковский счет!"' + "\033[0m")

class BankAccount:
    def __init__(self, account, balance):
        super().__init__()
        self.balance = balance
        self.account = account
        self.lock = Lock()
    def deposit(self, amount):
        with self.lock:  # Используем блокировку
            self.balance += amount
            print(f" Deposited {amount} New balance is {self.balance} ")

    def withdraw(self, amount):
        with self.lock:  # Используем блокировку
            if self.balance >= amount:
                self.balance -= amount
                print(f" Withdrew  {amount} New balance is {self.balance} ")
            else:
                print(f" Недостаточно средств для снятия {amount}. Balance is {self.balance}")

# Функция для выполнения задачи по депозиту
def deposit_task(account, amount):
    for i in range(5):
        account.deposit(amount)
        sleep(1)

# Функция для выполнения задачи по снятию денег
def withdraw_task(account, amount):
    for i in range(5):
        account.withdraw(amount)
        sleep(1)


account = BankAccount("Main Account", 1000)

deposit_thread = Thread(target=deposit_task, args=(account, 100))
deposit_thread.start()
deposit_thread.join()

withdraw_thread = Thread(target=withdraw_task, args=(account, 150))
withdraw_thread.start()
withdraw_thread.join()


print("\033[91m" + f'Все операции выполнены!' + "\033[0m")