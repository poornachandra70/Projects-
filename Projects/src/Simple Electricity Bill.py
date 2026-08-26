units = int(input("Enter units: "))

if units <= 100:
    print("Bill = ₹100")
elif units <= 200:
    print("Bill = ₹200")
elif units <= 300:
    print("Bill = ₹300")
else:
    print("Bill = ₹500")