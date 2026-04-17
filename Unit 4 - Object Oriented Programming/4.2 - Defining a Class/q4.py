"""
Author: Dinesh Sinnathamby
Date: April 17th, 2026
Description: This is a simple program that demonstrates the use of an incrementing class variable, increasing the student ID by 1 every time a new Student object is created.
"""

class Student:
    
    studentid = 0
    
    def __init__(self):
        self.name = "Ryan"
        self.mood = "Content"
        Student.studentid += 1
        self.studentid = Student.studentid
        
    def show_up_late(self):
        self.mood = "Unhappy"
        
    def got_good_grade(self):
        self.mood = "Happy"
        
    def get_name(self):
        return self.name
    
    def get_mood(self):
        return self.mood
    
    def get_studentid(self):
        return self.studentid
    
def main():
    
    ryan = Student()
    big_ryan = Student()
    other_ryan = Student()
    print(ryan.get_studentid(), big_ryan.get_studentid(),other_ryan.get_studentid())
    
    
main()