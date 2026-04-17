"""
Author: Dinesh Sinnathamby
Date: April 17th, 2026
Description: This is a simple program demonstrating the possibility to alter class attributes without using methods, and changing the attributes directly.
"""

class Student:
    
    def __init__(self):
        self.name = "Ryan"
        self.mood = "Content"
        
    def show_up_late(self):
        self.mood = "Unhappy"
        
    def got_good_grade(self):
        self.mood = "Happy"
        
    def get_name(self):
        return self.name
    
    def get_mood(self):
        return self.mood
    
def main():
    
    student = Student()
    student.mood = "Happy"
    print(student.get_mood())
    
main()