num1 = int(input ("Введіть перше число: "))
num2 = int(input ("Введіть друге число: "))
num3 = int(input ("Введіть третє число: "))
summa = num1 + num2 + num3
dobutok = num1 * num2 * num3
print (f"Сума чисел: {summa}")
print (f"Добуток чисел: {dobutok}")


# формула площі ромба через діагоналі: S = d1 * d2 / 2
d1 = float(input("Введіть довжину першої діагоналі: "))
d2 = float(input("Введіть довжину другої діагоналі: "))
area = (d1 * d2) / 2
print(f"Площа ромба: {area}")


number = int(input("Введіть чотиризначне число: "))
num1 = number // 1000           # Перша цифра
num2 = (number // 100) % 10     # Друга цифра
num3 = (number // 10) % 10      # Третя цифра
num4 = number % 10              # Четверта цифра
dobutok = num1 * num2 * num3 * num4
print(f"Добуток цифр: {dobutok}")