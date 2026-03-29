"""
Author: Dinesh Sinnathamby
Date: March 27th, 2026
Description: This program takes a string containing popular deserts, and splits each value by the > sign before finally placing them in a list.
"""

myString = "cookies>milk>fudge>cake>ice cream"
newList = list(myString.split('>'))
print(newList)