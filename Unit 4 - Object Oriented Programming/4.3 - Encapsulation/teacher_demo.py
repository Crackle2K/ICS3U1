"""
Author: Dinesh Sinnathamby
Date: April 21st, 2026
Description: This program uses my previous Teacher class to create a teacher, then attempt to change the mood to angry.
"""

from school import Teacher

def main():
    my_teacher = Teacher("Mr. Smith", "happy")
    
    print(my_teacher)

    my_teacher.__mood = "angry" 
    
    print(str(my_teacher))

main()