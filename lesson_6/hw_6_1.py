import string


letter_range = input("Введіть дві літери через дефіс: ")
letters = string.ascii_letters

if len(letter_range) == 3 and letter_range[1] == "-":
    first_letter = letter_range[0]
    last_letter = letter_range[2]

    first_index = letters.index(first_letter)
    last_index = letters.index(last_letter)

    print(letters[first_index:last_index + 1])
else:
    print("Помилка: введіть дві літери через дефіс, наприклад a-c.")


# "a-c" -> abc
# "a-a" -> a
# "s-H" -> stuvwxyzABCDEFGH
# "a-A" -> abcdefghijklmnopqrstuvwxyzA

