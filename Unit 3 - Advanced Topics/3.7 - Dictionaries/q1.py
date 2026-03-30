"""
Author: Dinesh Sinnathamby
Date: March 30th, 2026
Description: This is a simple program that counts all the words in a predermined text file, textfile.txt.
"""

def word_count(lines):
    counter = {}
    for line in lines:
        words = line.split() 
        for word in words:
            clean_word = word.strip(".,!?;:()").lower()
            if clean_word:
                if clean_word in counter:
                    counter[clean_word] += 1
                else:
                    counter[clean_word] = 1
    return counter
        
def main():
    file = open("Unit 3 - Advanced Topics/3.7 - Dictionaries/textfile.txt", "r")
    lines = file.readlines()
    file.close()
    
    frequencies = word_count(lines)
    
    output_file = open("report.txt", "w")
    for word, count in frequencies.items():
        output_file.write(str(word) + ':' + str(count) +"\n")
    output_file.close()

main()