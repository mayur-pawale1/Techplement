import string
import random

# Function to get valid integer input
def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))  # Prompt the user and read input
            if value <= 0:
                print("Value must be greater than zero.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Getting password length
length = get_integer_input("Enter password length: ")

# Character sets menu
print('''Choose character set(s) for password:

         1. Digits
         2. Letters (uppercase and lowercase)
         3. Special characters
         4. All (Digits + Letters + Special characters)
         5. Exit''')

# Initialize character list as a list
characterList = []

# Getting character set for password
while True:
    try:
        choice = get_integer_input("Pick a number: ")
        
        if choice == 1:
            characterList.extend(string.digits)
        elif choice == 2:
            characterList.extend(string.ascii_letters)
        elif choice == 3:
            characterList.extend(string.punctuation)
        elif choice == 4:
            characterList.extend(string.digits + string.ascii_letters + string.punctuation)
        elif choice == 5:
            if not characterList:
                print("Please select at least one character set.")
                continue
            else:
                break
        else:
            print("Please pick a valid option!")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Ensure at least one character set is selected
if not characterList:
    print("No character set selected. Exiting.")
    exit()

# Ensure password length matches user input
if length < len(characterList):
    print(f"Warning: Password length ({length}) is shorter than selected character set ({len(characterList)} characters).")

# Generate password ensuring uniqueness using random.sample
password = ''.join(random.sample(characterList, length))

# Printing password as a string
print("Generated Password:", password)