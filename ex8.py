ora = int(input("Introdu o oră (0–23): "))

if 0 <= ora < 6:
    print("Este noapte.")
elif 6 <= ora < 12:
    print("Este dimineață.")
elif 12 <= ora < 18:
    print("Este după-amiază.")
elif 18 <= ora < 24:
    print("Este seară.")
else:
    print("Ora introdusă nu este validă.")