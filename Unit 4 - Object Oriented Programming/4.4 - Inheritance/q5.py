"""
Author: Dinesh Sinnathamby
Date: April 21st, 2026
Description: This is a simple example of inheritance in Python, as I created a Cola class that inherits from the Beverage class.
"""


class Beverage:
    def __init__(self, bev_name):
        self.__bev_name = bev_name
        
class Cola(Beverage):
    def __init__(self):
        Beverage.__init__(self, "cola")