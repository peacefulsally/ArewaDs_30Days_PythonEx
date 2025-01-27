#Set Level 1
# Given sets and list

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Find the length of the set it_companies
length_it_companies = len(it_companies)
print(f"Length of it_companies: {length_it_companies}")

#Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(f"After adding 'Twitter': {it_companies}")

# Insert multiple IT companies at once to the set it_companies
new_companies = {'Tesla', 'Intel', 'Adobe'}
it_companies.update(new_companies)
print(f"After adding multiple companies: {it_companies}")

#Remove one of the companies from the set it_companies
it_companies.remove('Google') 
print(f"After removing 'Google': {it_companies}")