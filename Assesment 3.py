import math

def display_menu():
    print("\n--- Menu ---")
    print("Please enter the letter which corresponds with your choice:")
    print("a - Calculate the area of a rectangle")
    print("b - Calculate the area of a circle")
    print("c - Display a multiplication table")
    print("d - Find the mean of three numbers")


def calculate_rectangle_area():
    try:
        width = float(input("Enter the width: "))
        height = float(input("Enter the height: "))
        area = width * height
        print(f"The area of the rectangle is: {area:.2f}")
    except ValueError:
        print("Invalid input. Please enter numerical values.")

def calculate_circle_area():
    try:
        radius = float(input("Enter the radius: "))
        area = math.pi * (radius ** 2)
        print(f"The area of the circle is: {area:.2f}")
    except ValueError:
        print("Invalid input. Please enter a numerical value.")

def display_multiplication_table():
    try:
        number = int(input("Enter a number to display its multiplication table: "))
        print(f"--- Multiplication Table for {number} ---")
        for i in range(1, 11):
            print(f"{number} x {i} = {number * i}")
    except ValueError:
        print("Invalid input. Please enter an integer.")

def calculate_mean():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        num3 = float(input("Enter third number: "))
        mean = (num1 + num2 + num3) / 3
        print(f"The mean of {num1}, {num2}, and {num3} is: {mean:.2f}")
    except ValueError:
        print("Invalid input. Please enter numerical values.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice ").lower()

        if choice == 'a':
            calculate_rectangle_area()
        elif choice == 'b':
            calculate_circle_area()
        elif choice == 'c':
            display_multiplication_table()
        elif choice == 'd':
            calculate_mean()

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
