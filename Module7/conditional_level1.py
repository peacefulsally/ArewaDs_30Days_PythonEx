# Day 7 - 30 Days Of Python Challenge
# If Conditional Statement
#  enter the users age

age = int(input("Enter your age: "))

# Check if user is 18 or older
if age >= 18:
    print("You are old enough to learn to drive.")
else:
    years_to_wait = 18 - age
    print(f"You need {years_to_wait} more years to learn to drive.")


# Define my_age
my_age = 45

# Get your_age from user input
your_age = int(input("Enter your age: "))

# Compare the ages
if my_age > your_age:
    difference = my_age - your_age
    if difference == 1:
        print("I am 1 year older than you.")
    else:
        print(f"I am {difference} years older than you.")
elif my_age < your_age:
    difference = your_age - my_age
    if difference == 1:
        print("You are 1 year older than me.")
    else:
        print(f"You are {difference} years older than me.")
else:
    print("We are the same age.")

# Get two numbers from the user
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Compare the numbers
if a > b:
    print("a is greater than b")
elif a < b:
    print("a is smaller than b")
else:
    print("a is equal to b")