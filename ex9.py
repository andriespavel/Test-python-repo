luna = int(input("Introdu numărul lunii (1–12): "))

if luna in (12, 1, 2):
    print("Este: iarna.")
elif luna in (3, 4, 5):
    print("Este: primăvara.")
elif luna in (6, 7, 8):
    print("Este: vara.")
elif luna in (9, 10, 11):
    print("Este: toamna.")
else:
    print("Număr de lună invalid.")