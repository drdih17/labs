count = 0
summ = 0

f = True

while f:
    n = input("input: ")

    try:
        n = float(n)

        if n < 0:
            count += 1
            summ += n
        else:
            f = False
    except ValueError:
        print("not a number")


print(f"Answer is {summ / count}")


