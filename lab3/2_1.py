count = 0

f = True
while f:
    le = input("Input your input: ")
    if le:
        f = False
    else:
        print("Your input is not inputed - try again")

count = le.count(":")
le = le.replace(":", "%")
    

print(f"Result is {le} and changed {count} symbols")


    