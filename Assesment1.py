def assessment_1():
    distance = int(input("how many miles to your house"))


    if distance < 10:
        int(input(f"Your fare is free"))

    elif distance < 21:
        int(input("Your fare is £10"))

    elif distance < 31:
        int(input("your fare is £15"))
