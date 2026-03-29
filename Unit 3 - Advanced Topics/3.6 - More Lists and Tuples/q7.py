"""
Author: Dinesh Sinnathamby
Date: March 29th, 2026
Description: Simple program that iterates through each line to count words and characters, before finally calculating the averages.
"""

file = open("textfile.txt", "r")
lines = file.readlines()
file.close()

total_sentences = 0
total_words = 0
total_characters = 0

for line in lines:
    line = line.strip()
    if line != "":
        total_sentences += 1
        
        words_in_line = line.split()
        total_words += len(words_in_line)
        
        for word in words_in_line:
            total_characters += len(word)

if total_sentences > 0:
    avg_words_per_sentence = total_words / total_sentences
else:
    avg_words_per_sentence = 0

if total_words > 0:
    avg_chars_per_word = total_characters / total_words
else:
    avg_chars_per_word = 0

print("Average words per sentence: " + str(avg_words_per_sentence))
print("Average characters per word: " + str(avg_chars_per_word))