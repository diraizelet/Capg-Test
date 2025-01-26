# this function takes 
def getInput():
    num= int(input("Enter the number: "))
    if num<=0:
        print(" The input is invalid")
        exit
    return num


# the below commented code uses recurssions to perform factorial
# def doFactorial(num):
#     if num!=0:
#         return num*doFactorial(num-1)
#     return 1


"""do factorial has a while loop that counts down from number and everytime it counts 
down till 1 it multiplies itself to value store in the fact variable 
"""
def doFactorial(num):
    fact=1
    while num!=1:
        fact*=num
        num-=1
    return fact

def main():
    num=getInput()
    print(doFactorial(num))

main()