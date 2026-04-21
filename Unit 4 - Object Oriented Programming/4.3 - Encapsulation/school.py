"""
Author: Dinesh Sinnathamby
Date: April 21st, 2026
Description: This is a simple program that creates a Teacher class with their own mood, intended to be used in a seperate file as an import.

"""


class Teacher:
    def __init__(self, name, mood):
        self.__name = name
        self.__mood = mood

    def __str__(self):
        return f"{self.__name} is {self.__mood}"