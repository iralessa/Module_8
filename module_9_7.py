def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        if result <= 1:
            print(f"{result} - не является ни простым, ни составным числом")
        elif result <= 3:
            print(f"{result} - простое число")
        elif result % 2 == 0 or result % 3 == 0:
            print("Составное число")
        else:
            print("Простое число")
        return result
    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)

result = sum_three(2, 3, 6)
print(result)
