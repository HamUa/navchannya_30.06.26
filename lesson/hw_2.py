number = 5
number = number ** 2
print (number)


firsNumber = float(input("Введіть число: "))
secondNumber = float(input("Введіть число: "))
thirdNumber = float(input("Введіть число: "))
seredne = (firsNumber + secondNumber + thirdNumber) / 3
print (seredne)


time = int(input("Введіть кількість хвилин: "))
hours = time // 60
minutes_left = time % 60
print (hours, minutes_left)


cina = float(input("Введіть ціну: "))
znuzhka = float(input("Введіть знижку:"))
rozrachunokZnizhky = cina - (cina * znuzhka / 100)
print (rozrachunokZnizhky)


digit = int(input("Введіть число: "))
last_digit = digit % 10
print (last_digit)


length = float(input("Введіть довжину: "))
width_1 = float(input("Введіть штрину: "))
perimetr_1 = 2 * (length + width_1)
print (perimetr_1)


number_1 = int(input("Введіть 4‑значне число: "))
thousands = number_1 // 1000
hundreds = (number_1 // 100) % 10
tens = (number_1 // 10) % 10
units = number_1 % 10
print(thousands)
print(hundreds)
print(tens)
print(units)