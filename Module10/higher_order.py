
# Level one exercise
# Difference between map, filter, and reduce
# map: Applies a given function to all items in an input list and returns a list of the results
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared)

# filter: Applies a given function to all items in an input list and returns a list of items for which the function returns True.
numbers = [1, 2, 3, 4]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)

# reduce: Applies a given function cumulatively to the items of a list, from left to right, to reduce the list to a single value. It is part of the functools module.
from functools import reduce
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)

# Difference between higher-order function, closure, and decorator
# Higher-order function: A function that takes one or more functions as arguments or returns a function as a result.
def higher_order_function(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper
# Closure: A function object that remembers values in enclosing scopes even if they are not present in memory.
def outer_function(msg):
    def inner_function():
        print(msg)
    return inner_function

closure = outer_function("Hello, World!")
closure()

# Decorator: A special type of higher-order function that is used to modify the behavior of another function.
def decorator_function(original_function):
    def wrapper_function():
        print("Wrapper executed this before {}".format(original_function.__name__))
        return original_function()
    return wrapper_function

@decorator_function
def display():
    print("Display function ran")
display()

# Define a call function before map, filter, or reduce
def call_function(func, data):
    return func(data)

numbers = [1, 2, 3, 4]

# Using call_function with map
result_map = call_function(lambda x: list(map(lambda y: y**2, x)), numbers)
print(result_map)

# Using call_function with filter
result_filter = call_function(lambda x: list(filter(lambda y: y % 2 == 0, x)), numbers)
print(result_filter)

# Using call_function with reduce
from functools import reduce
result_reduce = call_function(lambda x: reduce(lambda y, z: y * z, x), numbers)
print(result_reduce)

# Use for loop to print each country in the countries list
countries = ['Finland', 'Sweden', 'Norway']
for country in countries:
    print(country)

# Use for loop to print each name in the names list
names = ['Asabeneh', 'David', 'Donald', 'Bill']
for name in names:
    print(name)

# Use for loop to print each number in the numbers list
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)

# Level two exercise
# Use map to create a new list by changing each country to uppercase in the countries list
countries = ['Finland', 'Sweden', 'Norway']
uppercased_countries = list(map(lambda country: country.upper(), countries))
print(uppercased_countries)

# Use map to create a new list by changing each number to its square in the numbers list
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)

# Use map to change each name to uppercase in the names list
names = ['Asabeneh', 'David', 'Donald', 'Bill']
uppercased_names = list(map(lambda name: name.upper(), names))
print(uppercased_names)

# Use filter to filter out countries containing 'land'
countries = ['Finland', 'Sweden', 'Norway', 'Iceland', 'Thailand']
countries_with_land = list(filter(lambda country: 'land' in country.lower(), countries))
print(countries_with_land)

# Use filter to filter out countries having exactly six characters
countries = ['Finland', 'Sweden', 'Norway', 'Iceland', 'Thailand']
six_char_countries = list(filter(lambda country: len(country) == 6, countries))
print(six_char_countries)

# Use filter to filter out countries containing six letters and more in the country list
countries = ['Finland', 'Sweden', 'Norway', 'Iceland', 'Thailand']
six_or_more_char_countries = list(filter(lambda country: len(country) >= 6, countries))
print(six_or_more_char_countries)

# Use filter to filter out countries starting with an 'E'
countries = ['Finland', 'Sweden', 'Norway', 'Iceland', 'Estonia']
countries_starting_with_e = list(filter(lambda country: country.startswith('E'), countries))
print(countries_starting_with_e)

# Chain two or more list iterators
numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))
print(result)

# Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items
def get_string_lists(lst):
    return list(filter(lambda x: isinstance(x, str), lst))

mixed_list = [1, 'hello', 3.14, 'world', True]
string_list = get_string_lists(mixed_list)
print(string_list)

# Use reduce to sum all the numbers in the numbers list
from functools import reduce

numbers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)

# Use reduce to concatenate all the countries and produce a sentence
from functools import reduce

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
sentence = reduce(lambda x, y: x + ', ' + y, countries[:-1]) + ', and ' + countries[-1] + ' are north European countries.'
print(sentence)

# Declare a function called categorize_countries that returns a list of countries with some common pattern
def categorize_countries(pattern):
    countries = ['Finland', 'Sweden', 'Norway', 'Iceland', 'Thailand', 'Estonia', 'Pakistan', 'India']
    return [country for country in countries if pattern in country.lower()]

print(categorize_countries('land'))
print(categorize_countries('ia'))
print(categorize_countries('stan'))

# Create a function returning a dictionary where keys are starting letters of countries and values are the number of country names starting with that letter
def count_countries_by_initial():
    countries = ['Finland', 'Sweden', 'Norway', 'Iceland', 'Thailand', 'Estonia', 'Pakistan', 'India']
    country_dict = {}
    for country in countries:
        initial = country[0].upper()
        if initial in country_dict:
            country_dict[initial] += 1
        else:
            country_dict[initial] = 1
    return country_dict

print(count_countries_by_initial())

# Declare a get_first_ten_countries function that returns a list of the first ten countries
def get_first_ten_countries():
    countries = ['Finland', 'Sweden', 'Norway', 'Iceland', 'Thailand', 'Estonia', 'Pakistan', 'India', 'China', 'Japan', 'Germany', 'France']
    return countries[:10]

print(get_first_ten_countries())

# Declare a get_last_ten_countries function that returns the last ten countries
def get_last_ten_countries():
    countries = ['Finland', 'Sweden', 'Norway', 'Iceland', 'Thailand', 'Estonia', 'Pakistan', 'India', 'China', 'Japan', 'Germany', 'France']
    return countries[-10:]

print(get_last_ten_countries())

# Exercise level three
# Sort countries by name, by capital, by population
import json

# Load the countries data
with open('countries-data.py') as f:
    countries_data = json.load(f)

# Sort by name
sorted_by_name = sorted(countries_data, key=lambda x: x['name'])
# Sort by capital
sorted_by_capital = sorted(countries_data, key=lambda x: x['capital'])
# Sort by population
sorted_by_population = sorted(countries_data, key=lambda x: x['population'], reverse=True)

print("Sorted by name:", sorted_by_name[:5])  # Displaying first 5 for brevity
print("Sorted by capital:", sorted_by_capital[:5])
print("Sorted by population:", sorted_by_population[:5])

# Sort out the ten most spoken languages by location
from collections import Counter

# Count the occurrences of each language
language_counter = Counter()
for country in countries_data:
    language_counter.update(country['languages'])

# Get the ten most common languages
most_spoken_languages = language_counter.most_common(10)
print("Ten most spoken languages:", most_spoken_languages)

# Sort out the ten most populated countries
# Already sorted by population in the previous step
most_populated_countries = sorted_by_population[:10]
print("Ten most populated countries:", most_populated_countries)