a = float(input("Introdu primul număr: "))
b = float(input("Introdu al doilea număr: "))


print("Adunare:", a + b)
print("Scădere:", a - b)
print("Înmulțire:", a * b)


if b == 0:
    print("Împărțire:", a / b)
    print("Restul împărțirii:", a % b)
else:
    print("Împărțire: imposibilă (împărțire la zero)")
    print("Restul împărțirii: imposibil (împărțire la zero)")