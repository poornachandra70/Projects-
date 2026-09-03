a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a < b and a < c:
    print("A is smallest")
elif b < a and b < c:
    print("B is smallest")
else:
    print("C is smallest")