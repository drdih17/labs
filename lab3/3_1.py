f = True
while f:
    le = input("Input your numbers divided by ' ': ")

    try:
        le_dih = list(map(int, le.split()))
        f = False
    except ValueError:
        print("some element is not an integer - try again")

print("Minimal element index is ", le_dih.index(min(le_dih)))