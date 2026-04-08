
def count(user_string, character, counter):

    if len(user_string) > 0:
        if user_string[0] == character:
            counter += 1
            count(user_string[1:], character, counter)
            
        else:
            count(user_string[1:], character, counter)
    else:
        print(counter)

def main():
    counter = 0
    user_string = input("Enter your string: ")
    desired_character = input("Enter your desired character: ")
    count(user_string, desired_character, counter)
    
main()