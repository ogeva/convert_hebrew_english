#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

# English to Hebrew mapping based on the macOS Hebrew keyboard layout
eng_to_heb = {
    # Top row (numbers)
    '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9', '0': '0', '-': '-', '=': '=',
    
    # Second row
    'q': '/', 'w': "'", 'e': 'ק', 'r': 'ר', 't': 'א', 'y': 'ט', 'u': 'ו', 'i': 'ן', 'o': 'ם', 'p': 'פ', '[': ']', ']': '[',
    
    # Third row
    'a': 'ש', 's': 'ד', 'd': 'ג', 'f': 'כ', 'g': 'ע', 'h': 'י', 'j': 'ח', 'k': 'ל', 'l': 'ך', ';': 'ף', "'": ',',
    
    # Fourth row
    'z': 'ז', 'x': 'ס', 'c': 'ב', 'v': 'ה', 'b': 'נ', 'n': 'מ', 'm': 'צ', ',': 'ת', '.': 'ץ', '/': '.',
    
    # Space and other common characters
    ' ': ' ', '\n': '\n', '\t': '\t'
}

# Create reverse mapping for Hebrew to English
heb_to_eng = {v: k for k, v in eng_to_heb.items()}

def detect_language(text):
    """Detect if text is primarily Hebrew or English"""
    hebrew_chars = sum(1 for c in text if c in heb_to_eng)
    english_chars = sum(1 for c in text if c in eng_to_heb)
    return "hebrew" if hebrew_chars > english_chars else "english"

def convert_text(text):
    """Convert text between English and Hebrew based on detected language"""
    language = detect_language(text)
    result = ""
    
    if language == "english":
        # Convert English to Hebrew
        for char in text:
            lower_char = char.lower()
            if lower_char in eng_to_heb:
                result += eng_to_heb[lower_char]
            else:
                result += char
    else:
        # Convert Hebrew to English
        for char in text:
            if char in heb_to_eng:
                result += heb_to_eng[char]
            else:
                result += char
    
    return result

if __name__ == "__main__":
    # Read input from stdin (from Automator)
    input_text = sys.stdin.read()
    
    # Convert the text
    output_text = convert_text(input_text)
    
    # Print the result to stdout (back to Automator)
    print(output_text, end="")