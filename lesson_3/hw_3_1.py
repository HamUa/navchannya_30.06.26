#варіант калькулятора через if - else
num1 = float(input("Введіть перше число: "))
operation = input("Введіть математичну дію (+, -, *, /): ")
num2 = float(input("Введіть друге число: "))
if operation == '+':
    result = num1 + num2
    print(f"Результат: {result}")
elif operation == '-':
    result = num1 - num2
    print(f"Результат: {result}")
elif operation == '*':
    result = num1 * num2
    print(f"Результат: {result}")
elif operation == '/':
    if num2 == 0:
        print("Помилка: Ділення на нуль неможливе!")
    else:
        result = num1 / num2
        print(f"Результат: {result}")
else:
    print("Помилка: Введено невідому математичну дію.")


# варіант калькулятора з match
num1 = float(input("Введіть перше число: "))
operation = input("Введіть математичну дію (+, -, *, /): ")
num2 = float(input("Введіть друге число: "))

match operation:
    case '+':
        print(f"Результат: {num1 + num2}")
    case '-':
        print(f"Результат: {num1 - num2}")
    case '*':
        print(f"Результат: {num1 * num2}")
    case '/':
        if num2 == 0:
            print("Помилка: Ділення на нуль неможливе!")
        else:
            print(f"Результат: {num1 / num2}")
    case _:
        print("Помилка: Введено невідому математичну дію.")