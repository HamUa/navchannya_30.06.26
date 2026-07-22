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


user_input = input("Введіть назву змінної: ")

allowed_punctuation = "_"
forbidden_punctuation = set(string.punctuation) - set(allowed_punctuation)

is_valid = True
if user_input[0].isdigit():
    is_valid = False
elif any(char.isupper() for char in user_input):
    is_valid = False
elif any(char.isspace() or char in forbidden_punctuation for char in user_input):
    is_valid = False
elif "__" in user_input:
    is_valid = False
elif user_input in keyword.kwlist:
    is_valid = False

print(is_valid)

# _ => True
# __ => False
# ___ => False
# x => True
# get_value => True
# get value => False
# get!value => False
# some_super_puper_value => True
# Get_value => False
# get_Value => False
# getValue => False
# 3m => False
# m3 => True
# assert => False
# assert_exception => True
