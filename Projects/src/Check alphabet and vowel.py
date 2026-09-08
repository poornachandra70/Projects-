ch = input("Enter character: ")

if ch.isalpha():
    if ch.lower() in "aeiou":
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Not an alphabet")