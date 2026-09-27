text = input("Enter text: ")

uppercase = 0
lowercase = 0
digits = 0
spaces = 0
special = 0

for char in text:

    if char.isupper():
        uppercase += 1

    elif char.islower():
        lowercase += 1

    elif char.isdigit():
        digits += 1

    elif char.isspace():
        spaces += 1

    else:
        special += 1

print("Uppercase:", uppercase)
print("Lowercase:", lowercase)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special Characters:", special)