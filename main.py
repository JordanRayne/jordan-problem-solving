

# # def assessment_1():
# #
#     order_value = 50.00
#     distance = float(input("Please enter the delivery distance in miles: "))
#
#
#     if distance <= 10:
#         delivery_fee = 0
#     elif distance <= 20:
#         delivery_fee = 10
#     elif distance <= 30:
#         delivery_fee = 15
#     else:
#         delivery_fee = 20
#
#
#     print(f"\nOrder Value: £{order_value:.2f}")
#     print(f"Distance: {distance} miles")
#     print(f"Delivery Fee: £{delivery_fee:.2f}")
#
#
# def assessment_2():
#     number = int(input("pick a number between 1and 20"))
#     for i in range(1, 21):
#
#         if number == i:
#             print("x", end="")
#
#         else:
#             print("-", end="")
#
#
# def assessment_3():
#     import math
#
#     def display_menu():
#         print("\n--- Menu ---")
#         print("Please enter the letter which corresponds with your choice:")
#         print("a - Calculate the area of a rectangle")
#         print("b - Calculate the area of a circle")
#         print("c - Display a multiplication table")
#         print("d - Find the mean of three numbers")
#
#     def calculate_rectangle_area():
#         try:
#             width = float(input("Enter the width: "))
#             height = float(input("Enter the height: "))
#             area = width * height
#             print(f"The area of the rectangle is: {area:.2f}")
#         except ValueError:
#             print("Invalid input. Please enter numerical values.")
#
#     def calculate_circle_area():
#         try:
#             radius = float(input("Enter the radius: "))
#             area = math.pi * (radius ** 2)
#             print(f"The area of the circle is: {area:.2f}")
#         except ValueError:
#             print("Invalid input. Please enter a numerical value.")
#
#     def display_multiplication_table():
#         try:
#             number = int(input("Enter a number to display its multiplication table: "))
#             print(f"--- Multiplication Table for {number} ---")
#             for i in range(1, 11):
#                 print(f"{number} x {i} = {number * i}")
#         except ValueError:
#             print("Invalid input. Please enter an integer.")
#
#     def calculate_mean():
#         try:
#             num1 = float(input("Enter first number: "))
#             num2 = float(input("Enter second number: "))
#             num3 = float(input("Enter third number: "))
#             mean = (num1 + num2 + num3) / 3
#             print(f"The mean of {num1}, {num2}, and {num3} is: {mean:.2f}")
#         except ValueError:
#             print("Invalid input. Please enter numerical values.")
#
#     def main():
#         while True:
#             display_menu()
#             choice = input("Enter your choice ").lower()
#
#             if choice == 'a':
#                 calculate_rectangle_area()
#             elif choice == 'b':
#                 calculate_circle_area()
#             elif choice == 'c':
#                 display_multiplication_table()
#             elif choice == 'd':
#                 calculate_mean()
#
#             else:
#                 print("Invalid choice, please try again.")
#
#     if __name__ == "__main__":
#         main()


# def assessment_4():
#         def draw_grid():
#
#             try:
#                 x = int(input("Please enter an X coordinate (a number between 1 and 10): "))
#                 y = int(input("Please enter a Y coordinate (a number between 1 and 10): "))
#             except ValueError:
#                 print("Please enter valid integers.")
#                 return
#
#
#             if not (1 <= x <= 10) or not (1 <= y <= 10):
#                 print("Coordinates must be between 1 and 10.")
#                 return
#
#
#             for row in range(1, 11):
#                 line = []
#                 for col in range(1, 11):
#
#                     if row == y and col == x:
#                         line.append("X")
#                     else:
#                         line.append("-")
#                 print(" ".join(line))
#
#
#         draw_grid()

# def assessment_5():
    number_list = []

    while True:

        print("\n--- Menu ---")
        print("A - Add numbers")
        print("B - Display all values")
        print("C - Replace one number")
        print("D - Calculate the mean")

        choice = input("Please enter your choice from the following menu (A/B/C/D): ").upper()

        if choice == 'A':
            try:
                count = int(input("How many numbers do you wish to add? "))
                for i in range(count):
                    num = float(input(f"Enter number {i + 1}: "))
                    number_list.append(num)
                print("Numbers added.")
            except ValueError:
                print("Invalid input. Please enter a number.")


        elif choice == 'B':
            if not number_list:
                print("The list is empty.")
            else:
                print("Current list:", number_list)


        elif choice == 'C':
            if not number_list:
                print("List is empty. Nothing to replace.")
            else:
                print(f"Current list: {number_list}")
                try:
                    index = int(input(f"Enter the index (0 to {len(number_list) - 1}) to replace: "))
                    if 0 <= index < len(number_list):
                        new_val = float(input("Enter the new number: "))
                        number_list[index] = new_val
                        print("Value replaced.")
                    else:
                        print("Invalid index.")
                except ValueError:
                    print("Invalid input.")


        elif choice == 'D':
            if not number_list:
                print("List is empty. Cannot calculate mean.")
            else:
                mean = sum(number_list) / len(number_list)
                print(f"The mean of the list is: {mean:.2f}")

if __name__ == "__main__":
    main()


# def assessment_6():
#     numbers = [6, 5, 3, 1, 2]
#     for values in numbers:
#         print(f"current element: {values}, element 0: {numbers[0]}")
#
#
# def assessment_7():
#     class Character:
#         def __init__(self, name, health, attack, defence):
#             self.name = name
#
#             self.health = max(0, min(100, health))
#             self.attack = attack
#             self.defence = defence
#
#         def info(self):
#             return f"Character: {self.name} | HP: {self.health} | ATK: {self.attack} | DEF: {self.defence}"
#
#         def take_damage(self, amount):
#             # Damage is reduced by defence, but cannot be less than 0 effective_damage = max(0, amount - self.defence)
#             self.health -= effective_damage
#             if self.health < 0:
#                 self.health = 0
#             print(f"{self.name} took {effective_damage} damage!")
#
#         def heal(self, amount):
#             self.health += amount
#             if self.health > 100:
#                 self.health = 100
#             print(f"{self.name} healed for {amount} points!")
#
#
#
#
#     hero = Character("Knight", 100, 20, 10)
#     villain = Character("Goblin", 50, 15, 2)
#
#
#     print(hero.info())
#     print(villain.info())
#
#
#     hero.take_damage(25)
#     villain.take_damage(20)
#
#
#     hero.heal(10)
#     villain.heal(50)
#
#
#     print("\nFinal Stats:")
#     print(hero.info())
#     print(villain.info())
#

if __name__ == "__main__":
    # Uncomment one of the lines below to test that assessment
    
    # print(assessment_1())
    # print(assessment_2())
    # print(assessment_3())
    # print(assessment_4())
    # print(assessment_5())
    # print(assessment_6())
    # print(assessment_7())
    pass