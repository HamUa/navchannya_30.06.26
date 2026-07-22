import string
import keyword

name = input()

valid = (
    name.isidentifier()
    and name not in keyword.kwlist
    and "__" not in name
    and not any(char.isupper() for char in name)
    and not any(char in string.punctuation and char != "_" for char in name)
)

print(valid)

