numbers = [1, 2, 3, 4, 6, 7, 8, 9, 10,]

n = len(numbers) + 1

expected_sum = n * (n + 1) // 2

actual_sum = sum(numbers)

missing = expected_sum - actual_sum

print("Numbers:", numbers)
print("Missing Number:", missing)