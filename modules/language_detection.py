# Banana language detection module

import re

def detect_language(text):
    # Define character frequencies for different languages
    language_freqs = {
        'english': {'a': 0.08167, 'b': 0.01492, 'c': 0.02782, 'd': 0.04253, 'e': 0.12702, 'f': 0.02228, 'g': 0.02015, 'h': 0.06094, 'i': 0.06966, 'j': 0.00153, 'k': 0.00772, 'l': 0.04025, 'm': 0.02406, 'n': 0.06749, 'o': 0.07507, 'p': 0.01929, 'q': 0.00095, 'r': 0.05987, 's': 0.06327, 't': 0.09056, 'u': 0.02758, 'v': 0.00978, 'w': 0.0236, 'x': 0.0015, 'y': 0.01974, 'z': 0.00074},
        'french': {'a': 0.0788, 'b': 0.0094, 'c': 0.0335, 'd': 0.0411, 'e': 0.1715, 'f': 0.0102, 'g': 0.0097, 'h': 0.0107, 'i': 0.0812, 'j': 0.0069, 'k': 0.0001, 'l': 0.0568, 'm': 0.0298, 'n': 0.0724, 'o': 0.0531, 'p': 0.0301, 'q': 0.0136, 'r': 0.0664, 's': 0.0815, 't': 0.0733, 'u': 0.0571, 'v': 0.0087, 'w': 0.0005, 'x': 0.0046, 'y': 0.0031, 'z': 0.0012},
        # Add more languages and their character frequencies
    }

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