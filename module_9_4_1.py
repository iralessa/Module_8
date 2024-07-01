def all_variants(text):
    length = len(text)
    # Генерация подстрок длины 1
    for start in range(length):
        yield text[start:start + 1]

    # Генерация подстрок длины 2
    for start in range(length - 1):
        yield text[start:start + 2]

    # Генерация подстрок длины больше двух
    for start in range(length - 2):  
        for end in range(start + 3, length + 1):
            yield text[start:end]
# Пример
text = "abc"
for variant in all_variants(text):
    print(variant)