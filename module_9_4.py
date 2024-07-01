def all_variants(text):
    length = len(text)
    # Генерация подстрок длины 1
    for start in range(length):
        yield text[start:start + 1]

    # Генерация подстрок длины 2 и больше
    for start in range(length - 1):
        for end in range(start + 2, length + 1):
            yield text[start:end]

# Пример вызова функции-генератора и итерации по его результатам
text = "abc"
for variant in all_variants(text):
    print(variant)