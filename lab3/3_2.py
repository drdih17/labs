f = True
while f:
    le = input("Input your numbers divided by ' ': ")

    try:
        le_dih = list(map(int, le.split()))
        f = False
    except ValueError:
        print("some element is not an integer - try again")

print(f"\n{"=" * 45}\n")


le_good = []
le_bad = []

for i in le_dih:
    if i > 0:
        le_good.append(i)
    else:
        le_bad.append(i)



print(f"Lesser or 0:\n{le_good}")
print("-" * 45)
print(f"Not greater than 0:\n{le_bad}")