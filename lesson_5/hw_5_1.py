import keyword
import string


def is_valid_variable_name(name: str) -> bool:
    if not name:
        return False

    if name[0].isdigit():
        return False

    if name in keyword.kwlist:
        return False

    if "__" in name:
        return False

    for symbol in name:
        if symbol.isupper():
            return False
        if symbol.isspace():
            return False
        if symbol in string.punctuation and symbol != "_":
            return False

    return True


if __name__ == "__main__":
    variable_name = input("Введіть можливе ім'я змінної: ")
    print(is_valid_variable_name(variable_name))


