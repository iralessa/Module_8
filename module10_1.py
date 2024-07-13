from threading import Thread
from time import sleep, time
from datetime import datetime
print("\033[93m" + f'10-ый модуль,Домашнее задание по теме "Создание потоков"' + "\033[0m")

def write_words(word_count, file_name):
    with open(file_name, 'w') as file:
        for i in range(1, word_count + 1):
            word = f"Какое-то слово № {i}\n"
            file.write(word)
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")
time_start = datetime.now()

# Вызов функций последовательно
time_1 = write_words(10, 'example1.txt')
time_2 = write_words(30, 'example2.txt')
time_3 = write_words(200, 'example3.txt')
time_4 = write_words(100, 'example4.txt')

time_end_func = datetime.now()
res_time = time_end_func - time_start
print("\033[92m" + f"Работа функции за: {res_time} секунд" + "\033[0m")
# Создание и запуск потоков
time_start1 = datetime.now()
threads = []
thread1 = Thread(target=write_words, args=(10, 'example5.txt'))
thread2 = Thread(target=write_words, args=(30, 'example6.txt'))
thread3 = Thread(target=write_words, args=(200, 'example7.txt'))
thread4 = Thread(target=write_words, args=(100, 'example8.txt'))

threads.append(thread1)
threads.append(thread2)
threads.append(thread3)
threads.append(thread4)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

end_time1 = datetime.now()
res_time = end_time1 - time_start1
print("\033[94m" + f"Работа потоков за: {res_time} секунд" + "\033[0m")


