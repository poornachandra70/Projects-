arr = [10, 15, 20, 25, 30]

count = 0

for x in arr:
    if x % 2 != 0:
        count = count + 1

print("Odd numbers =", count)