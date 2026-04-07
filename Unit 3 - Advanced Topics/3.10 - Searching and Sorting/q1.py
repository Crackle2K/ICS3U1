"""
Author: Dinesh Sinnathamby
Date: April 2nd, 2026
Description: This program demonstrates the use of an optimized bubble sort, and then demonstrates it using small as well as large lists.
"""

import random

def bubble_sort(aList):
    time = 0
    n = len(aList)
    dont_swap = True
    for j in range(n):
        for i in range(n - 1 - j):
            time += 1
            if aList[i] > aList[i+1]:
                temp = aList[i]
                aList[i] = aList[i+1]
                aList[i+1] = temp
                dont_swap = False
        if dont_swap:
            break

    print(aList, time)

# bubble_sort([5, 4, 7, 1, 10, 6, 8, 9, 16, 3, 0, 8, 9])


lst = []
for i in range(1000):
    lst.append(random.randint(1, 1000))
    
bubble_sort(lst)