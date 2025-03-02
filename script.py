import os
import re
from collections import Counter
import socket

# Function to read and process text files
def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        text = file.read().lower()  # Convert to lowercase for consistency
        # Split contractions and remove punctuation
        words = re.findall(r'\b\w+\b', text)
    return words

# Function to handle contractions (splitting them into individual words)
def handle_contractions(text):
    # Replace common contractions with their expanded versions
    replacements = {
        "i'm": "i am",
        "can't": "can not",
        "don't": "do not",
        "he's": "he is",
        "she's": "she is",
        "it's": "it is",
        "we're": "we are",
        "they're": "they are",
        "i've": "i have",
        "you've": "you have",
        "we've": "we have",
        "they've": "they have",
        "i'll": "i will",
        "you'll": "you will",
        "he'll": "he will",
        "she'll": "she will",
        "we'll": "we will",
        "they'll": "they will",
        "isn't": "is not",
        "aren't": "are not",
        "wasn't": "was not",
        "weren't": "were not",
        "hasn't": "has not",
        "haven't": "have not",
        "hadn't": "had not",
        "doesn't": "does not",
        "don't": "do not",
        "won't": "will not",
        "wouldn't": "would not",
        "can't": "cannot",
    }
    for contraction, expanded in replacements.items():
        text = text.replace(contraction, expanded)
    return text

# Function to get the IP address of the machine
def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

# Paths to the input files and output directory
data_dir = '/home/data'
if1_file = os.path.join(data_dir, 'IF-1.txt')
always_file = os.path.join(data_dir, 'AlwaysRememberUsThisWay-1.txt')
output_dir = os.path.join(data_dir, 'output')
output_file = os.path.join(output_dir, 'result.txt')

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Read and process both files
if1_words = read_file(if1_file)
always_words = read_file(always_file)

# Handle contractions in the 'AlwaysRememberUsThisWay-1.txt'
always_text = handle_contractions(' '.join(always_words))
always_words = re.findall(r'\b\w+\b', always_text.lower())

# a. Count total words in each file
if1_word_count = len(if1_words)
always_word_count = len(always_words)

# b. Calculate grand total of words
grand_total = if1_word_count + always_word_count

# c. Top 3 most frequent words in IF-1.txt
if1_word_freq = Counter(if1_words).most_common(3)

# d. Top 3 most frequent words in AlwaysRememberUsThisWay-1.txt (after handling contractions)
always_word_freq = Counter(always_words).most_common(3)

# e. Get IP address
ip_address = get_ip_address()

# f. Write detailed results to output file
with open(output_file, 'w', encoding='utf-8') as f:
    f.write("Project 3: Docker\n\n")
    
    # a. Word count for IF-1.txt
    f.write("a. Total number of words in each text file located at /home/data:\n")
    f.write(f"  IF-1.txt: {if1_word_count} words\n")
    f.write(f"  AlwaysRememberUsThisWay-1.txt: {always_word_count} words\n\n")
    
    # b. Grand total of words
    f.write("b. Calculate the grand total of words across both files:\n")
    f.write(f"  Grand Total: {grand_total} words\n\n")
    
    # c. Top 3 words in IF-1.txt
    f.write("c. Identify the top 3 most frequent words and their respective counts in IF-1.txt:\n")
    for word, count in if1_word_freq:
        f.write(f"   '{word}': {count} times\n")
    f.write("\n")
    
    # d. Top 3 words in AlwaysRememberUsThisWay-1.txt (with contractions split)
    f.write("d. Handle contractions (Examples: I'm, can't, don't) by splitting them into individual words:\n")
    f.write("   Top 3 Words in AlwaysRememberUsThisWay-1.txt (with contractions treated as separate words):\n")
    for word, count in always_word_freq:
        f.write(f"   '{word}': {count} times\n")
    f.write("\n")
    
    # e. Machine details (IP address)
    f.write("e. Determine the IP address of the machine running the container:\n")
    f.write(f"   IP Address: {ip_address}\n")

# Print the contents of result.txt to the console
with open(output_file, 'r', encoding='utf-8') as f:
    print(f.read())
