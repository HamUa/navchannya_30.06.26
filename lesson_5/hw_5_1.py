import keyword
import string

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
