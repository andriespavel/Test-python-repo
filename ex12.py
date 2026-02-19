varsta = int(input("Introdu vârsta: "))

if varsta <= 0 or varsta > 135:
    print("Vârstă invalidă.")
elif varsta < 12:
    print("Ești copil.")
elif varsta <= 18:
    print("Ești adolescent.")
else:
    print("Ești adult.")