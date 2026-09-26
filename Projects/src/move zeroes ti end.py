numbers = [0, 23, 45, 3, 12]

non_zero = [num for num in numbers if num != 0]
zeros = [0] * numbers.count(0)

result = non_zero + zeros

print(result)