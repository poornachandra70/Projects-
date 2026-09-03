a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))

if a*a + b*b == c*c:
    print("Right triangle")
else:
    print("Not a right triangle")