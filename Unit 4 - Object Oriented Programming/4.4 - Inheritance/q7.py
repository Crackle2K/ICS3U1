"""
Author: Dinesh Sinnathamby
Date: April 21st, 2026
Description: A Student class that inherits from Person, adding a student ID and cell phone status.
"""

class Person:

    def __init__(self, name, address, telephone):
        self.set_name(name)
        self.set_address(address)
        self.set_telephone(telephone)

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_address(self, address):
        self.__address = address

    def get_address(self):
        return self.__address

    def set_telephone(self, telephone):
        self.__telephone = telephone

    def get_telephone(self):
        return self.__telephone


class Student(Person):

    def __init__(self, name, address, telephone, student_id, has_cell_phone):
        Person.__init__(self, name, address, telephone)
        self.set_student_id(student_id)
        self.set_has_cell_phone(has_cell_phone)

    def set_student_id(self, student_id):
        self.__student_id = student_id

    def get_student_id(self):
        return self.__student_id

    def set_has_cell_phone(self, has_cell_phone):
        self.__has_cell_phone = bool(has_cell_phone)

    def get_has_cell_phone(self):
        return self.__has_cell_phone


def main():
    me = Student("Dinesh Sinnathamby", "123 Caldbeck, Toronto, ON", "647-555-0192", "348980830", True)

    print("Name:          ", me.get_name())
    print("Address:       ", me.get_address())
    print("Telephone:     ", me.get_telephone())
    print("Student ID:    ", me.get_student_id())
    print("Has cell phone:", me.get_has_cell_phone())


main()
