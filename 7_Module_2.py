def custom_write(file_name, strings):
    strings_positions = {}

    with open(file_name, 'w', encoding='utf-8') as file:
        for i, line in enumerate(strings, 1):
            byte_position = file.tell()  # Получаем текущую позицию в байтах
            file.write(line + '\n')  # Записываем строку в файл, добавляя новую строку
            strings_positions[(i, byte_position)] = line  # Добавляем в словарь

    return strings_positions


# Пример использования
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)  # Создаст файл 'test.txt' в текущем каталоге
for elem in result.items():
    print(elem)