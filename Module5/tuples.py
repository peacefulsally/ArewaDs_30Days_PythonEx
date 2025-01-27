# Tuples Exercise

sisters = ()
brothers = tuple()
sisters =('Bilkisu', 'Aisha', 'Zainab' )
brothers = ('Aliyu', 'Umar', 'Alamin', 'Sadiq')
siblings = sisters + brothers
print(f'my sisters are:{sisters}')
print(f'my sisters are:{brothers}')
print(f"my siblings are :{siblings}")
len(siblings)

#modify the tuple
parents = ('Baba', 'Mama')  # Names of parents
family_members = siblings + parents
print(f"Family members: {family_members}")

#Tuples level 2 excercises

#Unpack siblings and parents from family_members

family_members = ('Bilkisu', 'Aisha', 'Zainab', 'Aliyu', 'Umar', 'Alamin', 'Sadiq', 'Baba', 'Mama')
parents = ('Baba', 'Mama')  # Names of parents

#siblings, father, mother = family_members
print(f"Siblings: {siblings}")
print(f"parents: {parents}")

#Create fruits, vegetables, and animal products tuples
fruits = ('Apple', 'Banana', 'Orange', 'Mango', 'Pea')
vegetables = ('Carrot', 'Broccoli', 'Spinach')
animal_products = ('Milk', 'Cheese', 'Eggs')

# Join the three tuples into food_stuff_tp
food_stuff_tp = fruits + vegetables + animal_products
print(f"Food stuff tuple: {food_stuff_tp}")

#Change food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(f"Food stuff list: {food_stuff_lt}")

#Slice out the middle item or items
length = len(food_stuff_lt)
if length % 2 == 0:  # If even, take the two middle items
    middle_items = food_stuff_lt[length // 2 - 1:length // 2 + 1]
else:  # If odd, take the single middle item
    middle_items = food_stuff_lt[length // 2]
print(f"Middle item(s): {middle_items}")

#Slice out the first three and last three items from the list
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]
print(f"First three items: {first_three}")
print(f"Last three items: {last_three}")

#Delete the food_stuff_tp tuple completely
del food_stuff_tp
#print(food_stuff_tp)

#Check if an item exists in a tuple
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

# Check if 'Estonia' is a Nordic country
is_estonia_nordic = 'Estonia' in nordic_countries
print(f"Is Estonia a Nordic country? {is_estonia_nordic}")

# Check if 'Iceland' is a Nordic country
is_iceland_nordic = 'Iceland' in nordic_countries
print(f"Is Iceland a Nordic country? {is_iceland_nordic}")
