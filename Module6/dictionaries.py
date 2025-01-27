# Day  6 - 30 Days Of Python Challenge
# Dictionaries

# Create an empty dictionary called dog
dog = {}
print(f"dog dictionary: {dog}")

# Add name, color, breed, legs, age to the dog dictionary
dog["name"] = "Max"
dog["color"] = "Red"
dog["breed"] = "Golden Retriever"
dog["legs"] = 4
dog["age"] = 3
print(f"Dog dictionary: {dog}")

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city, and address as keys
student = {
    "first_name": "Javita",
    "last_name": "Dove",
    "gender": "Male",
    "age": 25,
    "marital_status": "Single",
    "skills": ["Python"],
    "country": "Nigerian",
    "city": "Kaduna",
    "address": "Nasarwa "
}
print(f"Student dictionary: {student}")

# Get the length of the student dictionary
student_length = len(student)
print(f"Length of the student dictionary: {student_length}")

# Get the value of skills and check the data type
skills = student["skills"]
skills_type = type(skills)
print(f"Skills: {skills}")
print(f"Data type of skills: {skills_type}")

#Modify the skills values by adding one or two skills
student["skills"].extend(["c++", "SQL"])  
print(f"Updated skills: {student['skills']}")

 #Get the dictionary keys as a list
student_keys = list(student.keys())
print(f"Student dictionary keys: {student_keys}")

# Get the dictionary values as a list
student_values = list(student.values())
print(f"Student dictionary values: {student_values}")

# Change the dictionary to a list of tuples using items() method
student_items = list(student.items())
print(f"Student dictionary as list of tuples: {student_items}")

# Delete one of the items in the dictionary
del student["address"]
print(f"Student dictionary after deleting 'address': {student}")

# Delete one of the dictionaries
del dog
print("Dog dictionary has been deleted.")
