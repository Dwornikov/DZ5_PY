def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent > 0:
        return base * power(base, exponent - 1)
    else:
        return 1 / power(base, -exponent)

A = int(input("Введите число A: "))
B = int(input("Введите степень B: "))

result = power(A, B)
print("Результат:", result)
