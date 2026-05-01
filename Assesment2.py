
number = int(input("pick a number between 1and 20"))
for i in range(1, 21):

    if number == i:
        print("x", end="")

    else:
        print("-", end="")