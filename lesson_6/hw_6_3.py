user_number = input("Введіть ціле число: ")

while int(user_number) > 9:
    product = 1
    for digit in user_number:
        product *= int(digit)
    user_number = str(product)

print(int(user_number))


# 999 -> 2 # Ось чому - 999 розбиваємо на цифри і перемножуємо 9 * 9 * 9 = 729, Потім 7 * 2 * 9 = 126, потім 1 * 2 * 6 = 12 і в результаті 1 * 2 = 2
# 1000 -> 0
# 423 -> 8
# 33 -> 9
# 25 -> 0
# 1 -> 1
