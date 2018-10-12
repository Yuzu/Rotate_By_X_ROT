'''Tim - 'Rotate By X' | 2018
This program is meant to portray my implementation of ROT, a letter substitution cipher which replaces a letter by the X letter after it. For example, ROT1 would turn A into B, c into d, and so forth.
'''

import string
import os

def main():
    
    procedure = input("Enter the source for your text! Enter 'f' for a file, and 'm' for manual input!\n")

    if procedure == "f" or procedure == "F":
        file = input("Make sure the file is in the same directory as this script.\nEnter the name of the file, including the extension!\n")
        try:
            with open(file, "r") as f:
                userstring = f.read()
                
        except FileNotFoundError: # Will result from no extension. 
            
            for x in os.listdir():
                if file == x.split(".")[0]:
                    print("You didn't enter the extension. :( \nBut that's okay! Make sure to follow instructions next time.\n")
                    try:
                        with open(x, "r") as f:
                            userstring = f.read()
                    except Exception as e:
                        print("There has been an error! {0}".format(e))
                        
        except Exception as e:
            print("There has been an error! {0}".format(e))

    elif procedure == "m" or procedure == "M":
        userstring = input("Enter the string to be parsed.\n").replace('"', r'\"') # Sanitizes inputs w/ double quotes


    unicode = (ord(x) for x in userstring)

    rotlevel = int(input("What level of ROT do you want to convert to?\n"))

    rotstring = ""
    for x in unicode:

        # First condition checks if it overflows past 122, 122 = z
        # Second condition checks if the letter is between a-z to prevent conflict w/ elif
        
        if x+rotlevel > 122 and 97 <= x and x <= 122:
            x = (x + rotlevel) % 122  + 96 # If overflows, want to find by how much, and add it to a to prevent overflow
            
        # Same as above applies here
        elif x+rotlevel > 90 and 65 <= x <= 90:
            x = (x + rotlevel) % 90 + 64

        elif chr(x) not in string.ascii_letters:
            pass

        else:
            x += rotlevel

        rotstring += chr(x)

    with open("output.txt", "w") as f:
        f.write(rotstring.replace('\\"', r'"')) # Undoes sanitization

    print("Your output has been stored in 'output.txt'!")


if __name__ == "__main__":
    main()


