#This is Conditional Statement Level2 Excersises

def get_grade(score):
    score = int(score)
    if 80 <= score <= 100:
        return 'A'
    elif 70 <= score <= 79:
        return 'B'
    elif 60 <= score <= 69:
        return 'C'
    elif 50 <= score <= 59:
        return 'D'
    else:
        return 'F'

# Example usage
score = 98
grade = get_grade(score)
print(f"The grade for score {score} is {grade}")

# Get user input for the month
month = input("Enter the month: ").strip().capitalize()

# Check the season
if month in ["September", "October", "November"]:
    print("The season is Autumn.")
elif month in ["December", "January", "February"]:
    print("The season is Winter.")
elif month in ["March", "April", "May"]:
    print("The season is Spring.")
elif month in ["June", "July", "August"]:
    print("The season is Summer.")
else:
    print("Invalid month. Please enter a valid month name.")

# List of fruits
fruits = ['banana', 'orange', 'mango', 'lemon']

# Get user input for a fruit
fruit = input("Enter the name of a fruit: ").lower()

# Check if the fruit exists in the list
if fruit in fruits:
    print("That fruit already exists in the list.")
else:
    fruits.append(fruit)  # Add the fruit to the list if it doesn't exist
    print("Fruit added to the list.")
    print(f"Modified list: {fruits}")
 