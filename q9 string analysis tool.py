#getString gets the input from the user
def getString():
    return input("Enter the string: ")


#ifNumbers returns true if the argument passed to it is a number
def ifNumbers(character):
    if character in "1234567890":
        return True
    return False


#ifSpecial returns true if the argument passed is a special character
def ifSpecial(character):
    if character in "!@#$%^&*()_|-+=[]:;/?>.<,'":
        return True
    return False


# ifVowel returns true if the argument passed is a vowel
def ifVowel(character):
    if character in "aeiouAEIOU":
        return True
    return False

# the function prints all the outputs
def printtheresults(vowels, consonants, special, numbers, alphachain):
    print(len(vowels), " are the number of the vowels in the string they are ", vowels)
    print(len(consonants), " are the number of the consonents in the string they are ", consonants)
    print(len(numbers), " are the number of the numbers in the string they are ", numbers)
    print(len(special), " are the number of the special in the string they are ", special)
    print(alphachain[::-1])

#the main function stores the results and calls the functions that perform the work
def main():
    vowels=[]
    consonants=[]
    special=[]
    numbers=[]
    alphachain=getString()
    for x in alphachain:
        if ifVowel(x):
            vowels.append(x)
        elif ifNumbers(x):
            numbers.append(x)
        elif ifSpecial(x):
            special.append(x)
        else:
            consonants.append(x)
    printtheresults(vowels, consonants, special, numbers, alphachain)
    
if __name__ == "__main__":
    main()