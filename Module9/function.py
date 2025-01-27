#MODULE 9 OF 30 Days of python programming

#Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(a, b):
    return a + b    
#Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(r):
    return 3.14 * r * r      
   
#Write a function called add_all_nums which takes an arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*args):
    sum = 0
    for i in args:
        if type(i) == int:
            sum += i
        else:
            return "Invalid input"
    return sum

def convert_celsius_to_fahrenheit  (celsius):
    return (celsius * 9/5) + 32 

def check_season (month):
    if month in ['September', 'October', 'November']:
        return 'Autumn'
    elif month in ['December', 'January', 'February']:
        return 'Winter'
    elif month in ['March', 'April', 'May']:
        return 'Spring'
    elif month in ['June', 'July', 'August']:
        return 'Summer'
    else:
        return 'Invalid input'
    
def calculate_slope ():
    x1 = int(input('Enter x1: '))
    y1 = int(input('Enter y1: '))
    x2 = int(input('Enter x2: '))
    y2 = int(input('Enter y2: '))
    return (y2-y1)/(x2-x1)

def solve_quadratic_eqn ():
    a = int(input('Enter a: '))
    b = int(input('Enter b: '))
    c = int(input('Enter c: '))
    x1 = (-b + ((b**2) - 4*a*c)**0.5) / 2*a
    x2 = (-b - ((b**2) - 4*a*c)**0.5) / 2*a
    return x1, x2

def print_list():
    lst = [1, 2, 3, 4]
    for i in lst:
        print(i)

def reverse_list(arr):
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr

print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list(["A", "B", "C"]))
# ["C", "B", "A"]

def reverse_list():
    lst = [1, 2, 3, 4]
    return lst[::-1]

def capitalize_list_items(lst):
    return [item.capitalize() for item in lst]

def add_item(lst, item):
    lst.append(item)
    return lst

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))     

numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))

def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango')) 

numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))

def sum_of_numbers(n):
    return sum(range(1, n + 1))

print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050

def sum_of_odds(n):
    return sum(i for i in range(1, n + 1) if i % 2 != 0)

def sum_of_even(n):
    return sum(i for i in range(1, n + 1) if i % 2 == 0)


# Level 2 Exercise
def evens_and_odds(n):
    evens = sum(1 for i in range(n + 1) if i % 2 == 0)
    odds = n + 1 - evens
    return f"The number of odds are {odds}.\nThe number of evens are {evens}."

print(evens_and_odds(100))

import math
import statistics

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
# Call your function is_empty, it takes a parameter and it checks if it is empty or not

def is_empty(param):
    return not bool(param)

def calculate_mean(lst):
    return sum(lst) / len(lst)

def calculate_median(lst):
    return statistics.median(lst)

def calculate_mode(lst):
    return statistics.mode(lst)

def calculate_range(lst):
    return max(lst) - min(lst)

def calculate_variance(lst):
    return statistics.variance(lst)

def calculate_std(lst):
    return statistics.stdev(lst)


# Level 3 of Function Exercise
# Question 1 
def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Question 2
def all_unique(lst):
    """Check if all items in the list are unique."""
    return len(lst) == len(set(lst))

# Question 3
def all_same_type(lst):
    """Check if all items in the list are of the same data type."""
    return all(isinstance(x, type(lst[0])) for x in lst)

# Question 4
def is_valid_variable(var):
    """Check if the provided variable is a valid Python variable name."""
    import keyword
    if not var.isidentifier() or keyword.iskeyword(var):
        return False
    return True

## List Comparison
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtered_numbers = [num for num in numbers if num <= 0]
print(filtered_numbers)

list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list = [item for sublist in list_of_lists for inner_list in sublist for item in inner_list]
print(flattened_list)

list_of_tuples = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print(list_of_tuples)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened_countries = [[country.upper(), country[:3].upper(), capital.upper()] for sublist in countries for country, capital in sublist]
print(flattened_countries)

countries_dict = [{'country': country.upper(), 'city': capital.upper()} for sublist in countries for country, capital in sublist]
print(countries_dict)

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
concatenated_names = [f"{first} {last}" for sublist in names for first, last in sublist]
print(concatenated_names)

# Lambda function to calculate the slope (m) given two points (x1, y1) and (x2, y2)
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)

# Lambda function to calculate the y-intercept (b) given the slope (m) and one point (x, y)
y_intercept = lambda m, x, y: y - m * x

# Example usage:
x1, y1 = 1, 2
x2, y2 = 3, 4
m = slope(x1, y1, x2, y2)
b = y_intercept(m, x1, y1)

print(f"Slope: {m}")
print(f"Y-Intercept: {b}")