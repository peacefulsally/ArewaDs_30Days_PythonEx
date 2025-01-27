#MODULE 11 OF 30 Days of python programming

def count_lines_and_words(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        num_lines = len(lines)
        num_words = sum(len(line.split()) for line in lines)
    return num_lines, num_words

# Read and count lines and words for each file
files = ['data/obama_speech.txt', 'data/michelle_obama_speech.txt', 'data/donald_speech.txt', 'data/melina_trump_speech.txt']
results = {}

for file in files:
    num_lines, num_words = count_lines_and_words(file)
    results[file] = {'lines': num_lines, 'words': num_words}

print(results)

import json
from collections import Counter

def most_spoken_languages(filename, top_n):
    with open(filename, 'r') as file:
        countries_data = json.load(file)
    
    languages_counter = Counter()
    
    for country in countries_data:
        languages_counter.update(country['languages'])
    
    most_common_languages = languages_counter.most_common(top_n)
    return most_common_languages

# Example usage
print(most_spoken_languages(filename='./data/countries_data.json', top_n=10))

def most_populated_countries(filename, top_n):
    with open(filename, 'r') as file:
        countries_data = json.load(file)
    
    sorted_countries = sorted(countries_data, key=lambda x: x['population'], reverse=True)
    most_populated = sorted_countries[:top_n]
    return [(country['name'], country['population']) for country in most_populated]

# Example usage
print(most_populated_countries(filename='./data/countries_data.json', top_n=10))


import re
def extract_email_addresses(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    
    # Use regex to find all email addresses
    email_addresses = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', content)
    
    return email_addresses

# Example usage
email_addresses = extract_email_addresses('email_exchange_big.txt')
print(email_addresses)

from collections import Counter
import re

def find_most_common_words(text_or_file, num_words):
    # Check if the input is a file path or a string
    try:
        with open(text_or_file, 'r') as file:
            text = file.read()
    except FileNotFoundError:
        text = text_or_file
    
    # Use regex to find all words
    words = re.findall(r'\b\w+\b', text.lower())
    
    # Count the frequency of each word
    word_counts = Counter(words)
    
    # Get the most common words
    most_common_words = word_counts.most_common(num_words)
    
    return most_common_words

# Example usage
text = "This is a test. This test is only a test."
print(find_most_common_words(text, 3))

# Assuming the speeches are stored in text files
obama_speech = 'obama_speech.txt'
michelle_speech = 'michelle_speech.txt'
trump_speech = 'trump_speech.txt'
melania_speech = 'melania_speech.txt'

# Find the ten most frequent words in each speech
obama_common_words = find_most_common_words(obama_speech, 10)
michelle_common_words = find_most_common_words(michelle_speech, 10)
trump_common_words = find_most_common_words(trump_speech, 10)
melania_common_words = find_most_common_words(melania_speech, 10)

print("Obama's speech:", obama_common_words)
print("Michelle's speech:", michelle_common_words)
print("Trump's speech:", trump_common_words)
print("Melania's speech:", melania_common_words)

import re
from collections import Counter
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS # type: ignore
from sklearn.feature_extraction.text import TfidfVectorizer # type: ignore
from sklearn.metrics.pairwise import cosine_similarity # type: ignore

def clean_text(text):
    # Remove non-alphanumeric characters and convert to lowercase
    text = re.sub(r'\W+', ' ', text).lower()
    return text

def remove_support_words(text):
    # Remove stop words
    words = text.split()
    words = [word for word in words if word not in ENGLISH_STOP_WORDS]
    return ' '.join(words)

def check_text_similarity(text1, text2):
    # Clean and remove support words from both texts
    text1 = remove_support_words(clean_text(text1))
    text2 = remove_support_words(clean_text(text2))
    
    # Vectorize the texts
    vectorizer = TfidfVectorizer().fit_transform([text1, text2])
    vectors = vectorizer.toarray()
    
    # Compute cosine similarity
    similarity = cosine_similarity(vectors)
    return similarity[0][1]

# Example usage
with open(michelle_speech, 'r') as file:
    michelle_text = file.read()
with open(melania_speech, 'r') as file:
    melania_text = file.read()

similarity_score = check_text_similarity(michelle_text, melania_text)
print(f"Similarity between Michelle's and Melania's speeches: {similarity_score}")

# Find the 10 most repeated words in the romeo_and_juliet.txt
romeo_and_juliet = 'romeo_and_juliet.txt'
romeo_and_juliet_common_words = find_most_common_words(romeo_and_juliet, 10)

print("Romeo and Juliet:", romeo_and_juliet_common_words)

import pandas as pd # type: ignore

# Read the hacker news CSV file
hacker_news_df = pd.read_csv('hacker_news.csv')

# Count the number of lines containing 'python' or 'Python'
python_count = hacker_news_df['title'].str.contains(r'\b[Pp]ython\b', regex=True).sum()

# Count the number of lines containing 'JavaScript', 'javascript' or 'Javascript'
javascript_count = hacker_news_df['title'].str.contains(r'\b[Jj]ava[Ss]cript\b', regex=True).sum()

# Count the number of lines containing 'Java' and not 'JavaScript'
java_count = hacker_news_df['title'].str.contains(r'\b[Jj]ava\b', regex=True) & ~hacker_news_df['title'].str.contains(r'\b[Jj]ava[Ss]cript\b', regex=True)
java_count = java_count.sum()

print(f"Number of lines containing 'python' or 'Python': {python_count}")
print(f"Number of lines containing 'JavaScript', 'javascript' or 'Javascript': {javascript_count}")
print(f"Number of lines containing 'Java' and not 'JavaScript': {java_count}")
