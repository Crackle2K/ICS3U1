"""
Author: Dinesh Sinnathamby
Date: March 29th, 2026
Description: Simple program with a function to expand a selected date, arranging it neatly in a formatted string.
"""

def expand_date(date_string):
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    
    parts = date_string.split("/")
    month_index = int(parts[0]) - 1
    day = parts[1]
    year = parts[2]
    
    month_name = months[month_index]
    
    return month_name + " " + day + ", " + year

def main():
    requested_date = input("Enter the date: ")
    formatted = expand_date(requested_date)
    print(formatted)
    
main()