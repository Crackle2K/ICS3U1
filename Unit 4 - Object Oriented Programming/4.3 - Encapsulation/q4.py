"""
Author: Dinesh Sinnathamby
Date: April 21st, 2026
Description: This is a simple program demonstrating the use of classes in Object-Oriented Programming, as I created a Pet class that is able to have its attributes changed, whilst still being protected by encapsulation.
"""

class Pet:
    def __init__(self, name, type, age):
        self.__name = name
        self.__type = type
        self.__age = age
        
    def set_name(self, new_name):
        self.__name = new_name
        
    def set_animal_type(self, new_animal):
        self.__type = new_animal
        
    def set_age(self, new_age):
        self.__age = new_age
    
    def get_name(self):
        return self.__name
    
    def get_animal_type(self):
        return self.__type
    
    def get_age(self):
        return self.__age
    
def main():
    fluffy = Pet("Fluffy", "Dog", 14)
    new_name = input("What should the pet's new name be: ")
    new_type = input("What should the pet's new animal type be: ")
    new_age = int(input("What should the pet's new age be: "))
    
    fluffy.set_name(new_name)
    fluffy.set_animal_type(new_type)
    fluffy.set_age(new_age)
    
    print("Your pet's name is", fluffy.get_name())
    print("Your pet is a", fluffy.get_animal_type())
    print("Your pet is", fluffy.get_age(), "years old")
    
main()