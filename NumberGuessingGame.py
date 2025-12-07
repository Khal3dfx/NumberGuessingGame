import random
import os

os.system('clear')

def DiffChoice():
    print("Welcome to the Number Guessing Game!")
    print("1) Easy   (1–20)")
    print("2) Medium (1–50)")
    print("3) Hard   (1–100)")

    while True:
        c = input("Choose difficulty: ")
        print()

        if not c.isdigit():
            print("Error: please enter numbers only! Try again.")
            continue
    
        c = int(c)

        if c < 1 or c > 3:
            print("Error: the answer should be 1, 2, or 3! Try again")
        if c in range(1,4):
            break

    match c:
        case 1:
            print("Welcome to easy difficulty!")
            print("I'm thinking of a number between 1 and 20.")
            print("Try to guess it!\n")
            x = random.randint(1, 20)
            num = 20
            return x, num
        case 2:
            print("Welcome to medium difficulty!")
            print("I'm thinking of a number between 1 and 50.")
            print("Try to guess it!\n")
            x = random.randint(1, 50)
            num = 50
            return x, num
        case 3:
            print("Welcome to hard difficulty!")
            print("I'm thinking of a number between 1 and 100.")
            print("Try to guess it!\n")
            x = random.randint(1, 100)
            num = 100
            return x, num

x, num = DiffChoice()

y = 0
i = 1

while True:
    y = input("Enter your guess: ")
    
    # Check if the input is only digits
    if not y.isdigit():
        print("Error: please enter numbers only! Try again.\n")
        continue

    # Now convert safely to int
    y = int(y)

    # Check range

    if y < 1 or y > num:
        print(f"Number has to be between 1 and {num}! Try again.\n")
        continue

    # Compare with the correct number
    if y < x:
        i += 1
        print("Too low! Try again.\n")
    elif y > x:
        i += 1
        print("Too high! Try again.\n")
    else:
        print("🎉 Correct! You guessed the number!")
        print(f"You found it in {i} attempts.")
        print(" ")
        
        choice = input("Do you want to play again? (y/n): ").lower()
        while choice not in ("y", "n"):
            print("Invalid input! Input has to be y or n. ")
            choice = input("Try again: ").lower()
        else:
            if choice == "y":
                os.system('clear')
                x, num = DiffChoice()
                i = 1
                y = 0
            else:
                print()
                print("Thanks for playing! Goodbye!\n")
                break
            


    


