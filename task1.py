numbers = []

for i in range(5):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

highest_value = max(numbers)

print("The highest value is:", highest_value)