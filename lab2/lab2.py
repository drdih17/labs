f = True
while f:
    dihdoh = input("\nMaterial Type:")
    try:

        dihdoh = int(dihdoh)

        if dihdoh not in range(1, 4):
            print("incorrect material")
            print("1 - Steel\n2 - Aluminum\n3 - Copper")
            continue
        f = False
    except ValueError:
        print("value must be an integer")
        print("1 - Steel\n2 - Aluminum\n3 - Copper")

match(dihdoh):
    case(1):
        mat = "Steel"
        p = 7850
    case(2):
        mat = "Aluminum"
        p = 2700
    case(3):
        mat = "Copper"
        p = 8900

f = True
while f:
    l = input("\nList length:")
    try:
        l = float(l)
        if l < 0.1 or l > 5:
            print("incorrect length")
            continue
        f = False
    except ValueError:
        print("value must be a number")

f = True
while f:
    w = input("\nList width:")
    try:
        w = float(w)
        if w < 0.1 or w > 3:
            print("incorrect width")
            continue
        f = False
    except ValueError:
        print("value must be a number")

f = True
while f:
    t = input("\nList thickness:")
    try:
        t = float(t)
        if t < 0.1 or t > 20:
            print("incorrect thickness")
            continue
        f = False
    except ValueError:
        print("value must be a number")

f = True
while f:
    q = input("\nList quantity:")
    try:
        q = int(q)
        if q < 1 or q > 1000:
            print("incorrect amount")
            continue
        f = False
    except ValueError:
        print("value must be an integer")

m = l * w * (t / 1000) * p * q

if t < 0.5:
    res = "Thin list"
elif 0.5 <= t <= 5:
    res = "Normal list"
else:
    res = "Thick list"

print("----------------------\n")
print(f"Material: {mat},\nMass: {m},\nThickness class: {res}")