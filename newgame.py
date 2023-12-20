
def start_game():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a dark forest. You see two paths ahead.")

    while True:
        choice = input("Which path will you choose? (1 or 2): ")

        if choice == "1":
            path_1()
            break
        elif choice == "2":
            path_2()
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

def path_1():
    print("You chose path 1. You come across a river.")

    while True:
        choice = input("What will you do? (1. Swim across, 2. Look for a bridge): ")

        if choice == "1":
            print("You swim across the river and reach the other side safely.")
            print("Congratulations! You completed the adventure!")
            break
        elif choice == "2":
            print("You search for a bridge but couldn't find one. Game Over!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

def path_2():
    print("You chose path 2. You encounter a ferocious tiger.")

    while True:
        choice = input("What will you do? (1. Fight, 2. Run away): ")

        if choice == "1":
            print("You try to fight the tiger but it overpowers you. Game Over!")
            break
        elif choice == "2":
            print("You wisely run away from the tiger and find a hidden treasure.")
            print("Congratulations! You completed the adventure!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

# Start the game
start_game()
