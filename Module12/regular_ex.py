#MODULE 12 OF 30 Days of python programming

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
# Clean the text
paragraph = paragraph.lower()  # Convert to lowercase
for char in ".,!?;":          # Remove punctuation
    paragraph = paragraph.replace(char, "")

# Split into words
words = paragraph.split()  # Turn the paragraph into a list of words

# Count each word
word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1  # If the word is already counted, add 1
    else:
        word_counts[word] = 1   # Otherwise, start the count at 1

# Find the most frequent word
most_frequent_word = max(word_counts, key=word_counts.get)  # Get the word with the highest count
count = word_counts[most_frequent_word]

print(f"'{most_frequent_word}' is the most frequent word which appears {count} times in the paragraph.")

import re
text = "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction."

points = list(map(int, re.findall(r"-?\d+", text)))

sorted_points = sorted(points)

distance = sorted_points[-1] - sorted_points[0]

print("Extracted Points:", points)
print("Sorted Points:", sorted_points)
print("Distance between the furthest particles:", distance)

#Exercise: Level 2
import re
import keyword

def is_valid_variable(var_name):
    if keyword.iskeyword(var_name):
        return False
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    return bool(re.match(pattern, var_name))
print(is_valid_variable('first_name'))  
print(is_valid_variable('first-name'))  
print(is_valid_variable('1first_name')) 
print(is_valid_variable('firstname'))   


#Exercise: Level 3
import re
from collections import Counter

# Function to clean the text
def clean_text(sentence):
    # Remove all non-alphanumeric characters except spaces
    cleaned = re.sub(r'[^\w\s]', '', sentence)
    # Remove extra spaces and return cleaned text
    return cleaned.strip()

# Function to find the most frequent words
def most_frequent_words(text):
    # Split the cleaned text into words
    words = text.split()
    # Count the frequency of each word
    word_counts = Counter(words)
    # Return the three most common words
    return word_counts.most_common(3)

# Original sentence
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

# Clean the text
cleaned_text = clean_text(sentence)
print(cleaned_text)

# Find the three most frequent words
frequent_words = most_frequent_words(cleaned_text)
print(frequent_words)