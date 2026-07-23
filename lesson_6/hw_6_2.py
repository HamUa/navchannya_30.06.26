seconds = int(input("Введіть кількість секунд (від 0 до 8640000): "))

days, rem = divmod(seconds, 86400)
hours, rem = divmod(rem, 3600)
minutes, secs = divmod(rem, 60)

if 11 <= days % 100 <= 14:
    day_word = "днів"
elif days % 10 == 1:
    day_word = "день"
elif days % 10 in (2, 3, 4):
    day_word = "дні"
else:
    day_word = "днів"

time_str = f"{hours:02d}:{minutes:02d}:{secs:02d}"

print(f"{days} {day_word}, {time_str}")

# 0 -> 0 днів, 00:00:00
# 224930 -> 2 дні, 14:28:50
# 466289 -> 5 днів, 09:31:29
# 950400 -> 11 днів, 00:00:00
# 1209600 -> 14 днів, 00:00:00
# 1900800 - > 22 дні, 00:00:00
# 8639999 -> 99 днів, 23:59:59
# 22493 -> 0 днів, 06:14:53
# 7948799 -> 91 день, 23:59:59
