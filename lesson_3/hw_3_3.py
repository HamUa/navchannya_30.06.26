numbers = [1, 2, 3, 4, 5, 6]
middle = len(numbers) // 2
if len(numbers) % 2 != 0:
    middle += 1
part1 = numbers[:middle]
part2 = numbers[middle:]
print(part1)
print(part2)
result = [part1, part2]
print(result)
