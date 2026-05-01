def main():

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
