def calculate(first_number: float, operator: str, second_number: float) -> float:
    match operator:
        case "+":
            return first_number + second_number
        case "-":
            return first_number - second_number
        case "*":
            return first_number * second_number
        case "/":
            if second_number == 0:
                raise ZeroDivisionError("Ділення на нуль неможливе!")
            return first_number / second_number
        case _:
            raise ValueError("Введено невідому математичну дію.")


if __name__ == "__main__":
    while True:
        try:
            first = float(input("Введіть перше число: "))
            operation = input("Введіть математичну дію (+, -, *, /): ").strip()
            second = float(input("Введіть друге число: "))
            result = calculate(first, operation, second)
            print(f"Результат: {result}")
        except ValueError as error:
            print(f"Помилка: {error}")
        except ZeroDivisionError as error:
            print(f"Помилка: {error}")

        answer = input("Бажаєте виконати ще одне обчислення? (y/n): ").strip().lower()
        if answer != "y":
            print("Роботу калькулятора завершено.")
            break
