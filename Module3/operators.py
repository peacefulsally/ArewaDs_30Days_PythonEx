# Day 3: 30 Days of python programming

# Declarations of Variables 
age = 34
hieght = 5.7

# Complex Numbers
complex_number = 2+2j
print(complex_number)

# User input
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area = 0.5 * base * height
print(f"The area of the triangle is {area}")

side_a = float(input("Enter the value of side a: "))
side_b = float(input("Enter the value of side b: "))
side_c = float(input("Enter the value of side c: "))
perimeter = side_a + side_b + side_c
print(f"The perimeter is: {perimeter}")

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
perimeter = 2 * (length + width)
print(f"The area of the rectangle is {area}")
print(f"The perimeter of the rectangle is {perimeter}")

import math
radius = float(input("Enter the radius of a circle: "))
area = math.pi * radius* radius 
circumference = 2 * math.pi * radius
print(f"The area of the circle is {area}")
print(f"The circumference of the circle is {circumference}")

# Define the equation parameters
m = 2  # Slope of the line (coefficient of x)
b = -2  # Y-intercept (constant term)
# Calculate the slope
slope = m
# Calculate the x-intercept
# The x-intercept is when y = 0
x_intercept = -b / m
# The y-intercept is simply the constant term b
y_intercept = b

# Display the results
print(f"Slope: {slope}")
print(f"X-Intercept: ({x_intercept}, 0)")
print(f"Y-Intercept: (0, {y_intercept})")

import math
# Define the points
x1, y1 = 2, 2
x2, y2 = 6, 10
# Calculate the slope
slope = (y2 - y1) / (x2 - x1)
# Calculate the Euclidean distance
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
# Display the results
print(f"Slope: {slope}")
print(f"Euclidean Distance: {distance}")

# The values of task 8 and task 9 are as 
slope_task8 = 2
slope_task9 = 2
# Compare the slopes
if slope_task8 == slope_task9:
    print(f"The slopes are equal: {slope_task8}")
else:
    print(f"The slopes are different. Task 1 Slope: {slope_task8}, Task 2 Slope: {slope_task9}")

# Define the quadratic function
def calculate_y(x):
    return x**2 + 6*x + 9
# Test the function with various x values
x_values = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1]
for x in x_values:
    y = calculate_y(x)
    print(f"For x = {x}, y = {y}")

# Verify when y = 0
x_when_y_is_zero = -3
y_at_zero = calculate_y(x_when_y_is_zero)
print(f"\nWhen x = {x_when_y_is_zero}, y = {y_at_zero}")

# Strings
word1 = "python"
word2 = "dragon"
# Find lengths
length_word1 = len(word1)
length_word2 = len(word2)
# Falsy comparison statement
comparison = length_word1 != length_word2  # This is False since the lengths are equal
# Print the results
print(f"Length of '{word1}': {length_word1}")
print(f"Length of '{word2}': {length_word2}")
print(f"Falsy comparison (length_word1 != length_word2): {comparison}")

# both words are Strings
word1 = "python"
word2 = "dragon"

# Check if 'on' is in both words using the 'and' operator
result = ('on' in word1) and ('on' in word2)

# Print the result
print(f"Is 'on' found in both '{word1}' and '{word2}'? {result}")

# Sentence
sentence = "I hope this course is not full of jargon."

# Check if 'jargon' is in the sentence
result = 'jargon' in sentence

# Print the result
print(f"Is 'jargon' in the sentence? {result}")

# Strings
word1 = "python"
word2 = "dragon"

# Check if 'on' is in both words
is_in_python = 'on' in word1
is_in_dragon = 'on' in word2

# Print the results
print(f"Is 'on' in 'python'? {is_in_python}")
print(f"Is 'on' in 'dragon'? {is_in_dragon}")
print(f"Is 'on' in both 'python' and 'dragon'? {is_in_python and is_in_dragon}")

word = "python"

# To Find the length of the word we use
length = len(word)

# Convert the length to a float
length_float = float(length)

# Convert the float value to a string
length_string = str(length_float)

# Print the results
print(f"Length of '{word}': {length}")
print(f"Length as a float: {length_float}")
print(f"Length as a string: '{length_string}'")

# Input: Get the number from the user
number = int(input("Enter a number: "))

# Check if the number is even
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is not an even number.")

# Perform floor division of 7 by 3
floor_division_result = 7 // 3

# Convert 2.7 to an integer
int_value = int(2.7)

# Check if they are equal
comparison = floor_division_result == int_value

# Print the results
print(f"Floor division of 7 by 3: {floor_division_result}")
print(f"Integer value of 2.7: {int_value}")
print(f"Are they equal? {comparison}")

# Values
value1 = '10' 
value2 = 10   

# Check types
type_value1 = type(value1)
type_value2 = type(value2)

types_equal = type_value1 == type_value2

# Print the results
print(f"Type of '10': {type_value1}")
print(f"Type of 10: {type_value2}")
print(f"Are the types equal? {types_equal}")

# let check there type
value1 = '9.8'
value2 = 10
print(type(value1))
print(type(value2))

# Prompt the user to enter hours 
hours = float(input("Enter the number of hours worked: "))

# Prompt the user to enter the rate per hour
rate = float(input("Enter the rate per hour: "))

# Calculate the total pay
pay = hours * rate

# Display the total pay
print(f"Total pay is: N{pay}")

# Define constants
SECONDS_IN_A_YEAR = 365 * 24 * 60 * 60  # Seconds in a year (365 days)

# Prompt the user to enter the number of years
years = int(input("Enter the number of years: "))

# Calculate the number of seconds
seconds_lived = years * SECONDS_IN_A_YEAR

# Display the result
print(f"The number of seconds a person can live for {years} years is: {seconds_lived} seconds.")

# Print the header of the table
print("Number  Constant  Square  Cube  Power of 3")
# range = 1,2,3,4,5,
# Loop through the numbers from 1 to 5
for number in range(1, 6):
    constant = 1
    square = number ** 2
    cube = number ** 3
    power_of_3 = 3 ** number
    # Print the row in the table
    print(f"{number:<7} {constant:<9} {number:<7} {square:<6} {power_of_3:<10}")