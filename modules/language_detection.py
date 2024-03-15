# Banana language detection module

import json
import re


# Load language frequencies from JSON file
with open('resources/language_freqs.json', 'r') as file:
    language_freqs = json.load(file)


# Function to detect the language of text
def detect_language(text):
    # Remove non-alphabetic characters and convert to lowercase
    text = re.sub(r'[^a-zA-Z]', '', text.lower())
    
    # Calculate character frequencies in the text
    text_freqs = {}
    for char in text:
        if char in text_freqs:
            text_freqs[char] += 1
        else:
            text_freqs[char] = 1

    # Calculate total number of characters in the text
    total_chars = sum(text_freqs.values())
    
    # Calculate relative frequencies
    for char in text_freqs:
        text_freqs[char] /= total_chars

    # Calculate Euclidean distance between text and language frequencies
    distances = {}
    for lang, lang_chars in language_freqs.items():
        distance = 0
        for char, freq in lang_chars.items():
            if char in text_freqs:
                distance += (text_freqs[char] - freq) ** 2
            else:
                distance += freq ** 2
        distances[lang] = distance ** 0.5
    
    # Return the language with the smallest distance
    detected_language = min(distances, key=distances.get)
    return detected_language