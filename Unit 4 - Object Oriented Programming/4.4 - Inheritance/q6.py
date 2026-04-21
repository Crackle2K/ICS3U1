"""
Author: Dinesh Sinnathamby
Date: April 21st, 2026
Description: A Skeleton class that inherits from Monster, with a __hungry attribute.
"""

class Monster(object):

    def __init__(self, monster_name):
        self.set_name(monster_name)

    def set_name(self, monster_name):
        if monster_name:
            self.__name = monster_name
        else:
            self.__name = "Unknown"

    def get_name(self):
        return self.__name

    def speak(self):
        print("I am a monster named " + self.__name + ".")


class Skeleton(Monster):

    def __init__(self, monster_name, hungry):
        Monster.__init__(self, monster_name)
        self.set_hungry(hungry)

    def set_hungry(self, hungry):
        self.__hungry = bool(hungry)

    def get_hungry(self):
        return self.__hungry

    def speak(self):
        Monster.speak(self)
        if self.__hungry:
            print("And I am HUNGRY!")
        else:
            print("And I am not hungry.")


s1 = Skeleton("Bones", True)
s2 = Skeleton("Rattles", False)

s1.speak()
print()
s2.speak()
print()

print(s1.get_name(), "hungry?", s1.get_hungry())
s1.set_hungry(False)
print(s1.get_name(), "hungry after feeding?", s1.get_hungry())
