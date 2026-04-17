"""
Author: Dinesh Sinnathamby
Date: April 16th, 2026
Description: This is a simple program that demonstrates the use of a class, using a student named Ryan to change his mood based on various different methods.
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
    print (student.get_name(), "is", student.get_mood() )
    
    print ("\nOh no, a student just came in late!" )
    student.show_up_late()
    print (student.get_name(), "is", student.get_mood() )
    
    print ("\nGreat, we just aced our test!" )
    student.got_good_grade()
    print (student.get_name(), "is", student.get_mood() )
    
main()