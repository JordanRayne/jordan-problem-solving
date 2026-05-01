

def draw_grid():

    try:
        x = int(input("Please enter an X coordinate (a number between 1 and 10): "))
        y = int(input("Please enter a Y coordinate (a number between 1 and 10): "))
    except ValueError:
        print("Please enter valid integers.")
        return


    if not (1 <= x <= 10) or not (1 <= y <= 10):
        print("Coordinates must be between 1 and 10.")
        return


    for row in range(1, 11):
        line = []
        for col in range(1, 11):

            if row == y and col == x:
                line.append("X")
            else:
                line.append("-")
        print(" ".join(line))


draw_grid()
