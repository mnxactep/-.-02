a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

sum = a + b
difference = a - b
product = a * b
average = (a + b) / 2
absolute_difference = max(abs(a), abs(b)) - min(abs(a), abs(b))
quotient = round(a / b, 2)

print("Сумма чисел:", sum)
print("Разность чисел:", difference)
print("Произведение чисел:", product)
print("Среднее арифметическое чисел:", average)
print("Разность максимального и минимального по модулю:", absolute_difference)
print("Частное чисел:", quotient)