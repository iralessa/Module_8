import time
from multiprocessing import Pool
from datetime import timedelta

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:  # Проверяем, пустая ли строка
                break
            all_data.append(line.strip())  # Добавляем строку в список, убирая лишние пробелы

if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    # Линейный вызов
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    linear_duration = time.time() - start_time
    print(f"Линейный вызов: {str(timedelta(seconds=linear_duration))}")

    # Многопроцессный вызов
    start_time = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    multiprocessing_duration = time.time() - start_time
    print(f"Многопроцессный вызов: {str(timedelta(seconds=multiprocessing_duration))}")