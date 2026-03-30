"""
Author: Dinesh Sinnathamby
Date: March 30th, 2026
Description: This is a menu-driven program that allows users to look up, add, redefine, and delete terms in a "Geek Translator" dictionary.
"""

def main():
    geek = {
        "404": "clueless. From the web error message 404, meaning page not found.", 
        "Googling": "searching the Internet for background information on a person.", 
        "Keyboard Plaque": "the collection of debris found in computer keyboards.", 
        "Link Rot": "the process by which web page links become obsolete.", 
        "Percussive Maintenance": "the act of striking an electronic device to make it work.", 
        "Uninstalled": "being fired. Especially popular during the dot-bomb era."
    }

    choice = ""
    while choice != "5":
        print("\nGEEK TRANSLATOR")
        print("1 - Look Up a Geek Term")
        print("2 - Add a Geek Term")
        print("3 - Redefine a Geek Term")
        print("4 - Delete a Geek Term")
        print("5 - Quit")
        
        choice = input("\nChoice: ")

        if choice == "1":
            term = input("Enter the term you want to look up: ")
            if term in geek:
                print(f"{term}: {geek[term]}")
            else:
                print("Sorry, I don't know that term.")

        elif choice == "2":
            term = input("Enter the new term: ")
            if term not in geek:
                definition = input("Enter the definition: ")
                geek[term] = definition
                print("The term has been added.")
            else:
                print("That term already exists! Try redefining it.")

        elif choice == "3":
            term = input("Enter the term to redefine: ")
            if term in geek:
                print(f"Current definition: {geek[term]}")
                new_def = input("Enter the new definition: ")
                geek[term] = new_def
                print("Term has been redefined.")
            else:
                print("That term doesn't exist! Try adding it.")

        elif choice == "4":
            term = input("Enter the term to delete: ")
            if term in geek:
                del geek[term]
                print("Okay, I deleted the term.")
            else:
                print("Sorry, I don't know that term.")

        elif choice == "5":
            print("Quitting program...")

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

main()