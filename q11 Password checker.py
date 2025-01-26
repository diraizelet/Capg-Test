import string
#global variables that are used to store the validity details of the pwd
uppers =False
lower=False
special=False
digit=False

#takes the input from the user
def getString():
    return input("Enter the string: ")

#takes the argument and compares it with multiple different characters and sets the conditions to true
def checker(x):
    global lower
    global uppers
    global digit
    global special
    if x in "1234567890":
        digit=True
    if x in string.ascii_lowercase:
        lower=True
    if x in string.ascii_uppercase:
        uppers=True
    if x in "!@#$%^&*()_|-+=[]:;/?>.<,'":
        special=True
        

#runs a loop to call the validation function and prints if the password is strong or weak
def main():
    pwd = getString()
    if len(pwd)<8:
        print("Weak password")
        exit
    for x in pwd:
        checker(x)
        if digit and lower and uppers and special:
            print("Strong password")
            break
    if digit and lower and uppers and special:
        exit
    else: 
        print("Weak password")


main()


    