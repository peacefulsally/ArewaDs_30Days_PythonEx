# Day 5: 30 Days of python programming

#Level 1
empty_list = list()
empty_list = []

#list with 5 items
shopping_list = ['meat', 'maggi', 'fish', 'beans', 'salt', 'rice','spaggetti']
print ( shopping_list)

#length of the list
print(len(shopping_list))

# Get the first item, the middle item and the last item of the list
print(shopping_list[0])
print(shopping_list[4])
print(shopping_list[5])

#Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['name', 32, 3.2, 'married', 'railway kano']
print(mixed_data_types)

#we are declaring a varible
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
print(len(it_companies))
print(it_companies[0])
print(it_companies[3])
print(it_companies[-1])

#modifiying a list
del it_companies[1]
print(it_companies)

#adding IT company
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.append('IT company')

#to add the company to the middle of the list
middle_index = len(it_companies) // 2
it_companies.insert(middle_index, 'IT company')
print(f"After inserting in the middle: {it_companies}")


# To Change one of the IT companies' names to uppercase (IBM excluded!)
it_companies[1] = it_companies[1].upper()  
print(f"After changing to uppercase: {it_companies}")

#Join the IT companies with the string '#;  '
joined_it_companies = '#; '.join(it_companies)
print(f"Joined companies: {joined_it_companies}")

#Check if a certain company exists in the list
company_to_check = 'IT company'
is_company_in_list = company_to_check in it_companies
print(f"{company_to_check} exist in the list? {is_company_in_list}")

#sort the list using sort()
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.sort()
it_companies.sort(reverse=True)
print(f"Sorted list: {it_companies}")
print(f"Reversed (descending order) list: {it_companies}")

#Slice out the first 3 companies from the list
first_three = it_companies[:3]
print(f"First 3 companies: {first_three}")

#Slice out the last 3 companies from the list
last_three = it_companies[-3:]
print(f"Last 3 companies: {last_three}")

#Slice out the middle IT company or companies from the list
length = len(it_companies)
if length % 2 == 0:  # Even number of companies
    middle_companies = it_companies[length//2 - 1 : length//2 + 1]
else:  # Odd number of companies
    middle_companies = [it_companies[length//2]]
print(f"Middle IT company/companies: {middle_companies}")

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
#Remove the first company
print(it_companies)
del it_companies[0]
print(it_companies)

#Remove the middle IT company or companies from the list
length = len(it_companies)
if length % 2 == 0:  # Even number of companies
    middle_start = length // 2 - 1
    del it_companies[middle_start:middle_start + 2] 
else:  # Odd number of companies
    middle_index = length // 2
    del it_companies[middle_index]  # Remove the single middle company
print(f"After removing the middle company/companies: {it_companies}")

#Remove the last IT company from the list
del it_companies[-1] 
print(f"After removing the last company: {it_companies}")

#Remove all IT companies from the list
it_companies.clear()  # Clear all elements from the list
print(f"After removing all companies: {it_companies}")

#Destroy the IT companies list
del it_companies  # Completely delete the list

# Join the two lists
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']

# Join the lists
joined_list = front_end + back_end
print(f"Joined list: {joined_list}")

#Copy the joined list and assign it to a new variable full_stack
full_stack = joined_list.copy()

# Insert Python and SQL after Redux
redux_index = full_stack.index('Redux')  # Find the index of 'Redux'
full_stack.insert(redux_index + 1, 'Python')  # Insert Python after Redux
full_stack.insert(redux_index + 2, 'SQL')  # Insert SQL after Python
print(f"Full stack after inserting Python and SQL: {full_stack}")

