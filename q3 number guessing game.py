#use randon lib to get a random int between 1 and 100
import random

#a global variable that is used to store the number we got form random lib
randomNoGenerated=999999999999

#checkthevalidity check the validity of the number generated as low, high or win
def checkthevalidity( guessed):
    if randomNoGenerated == guessed:
        print ("You Win!!!")
        return 1
    elif randomNoGenerated > guessed:
        print("Too Low")
        return 0
    elif randomNoGenerated < guessed:
        print("Too High")
        return 0


#main function calls the function till the user wins
if __name__ =="__main__":
    randomNoGenerated = random.randint(1, 100)
    while (1):
        guess=int(input("Enter your guess (between 1-100): "))
        if checkthevalidity(guess)==1:
            break
    