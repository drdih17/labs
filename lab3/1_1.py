import math

f = True
while f:
    a = input("A: ")
    try:
        a = float(a)
        f = False
    except ValueError:
        print("value is not a number")

f = True
while f:
    b = input("B: ")
    try:
        b = float(b)

        if b <= a:
            print("B must be bigger than A - Try again")
        else:
            f = False
    except ValueError:
        print("value is not a number")




a = math.ceil(a)
b = math.floor(b)

dih = 0

for i in range(a, b + 1):
    dih += i

print(f"Answer is {dih}")