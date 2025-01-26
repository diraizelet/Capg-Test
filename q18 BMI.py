# the function returns the bmi 
def BMI(weight, height):
    return weight/ (height**2)

#getInput gets the weight and height from the user
def getInput():
    weight=int(input("Enter the weight(kgs): "))
    height=int(input("Enter the height(m): "))
    return weight, height
#calls the input getter function and calls the BMI calculating function
def main():
    weight, height=getInput()
    bMI= BMI(weight,height)
    print("BMI:",bMI)


main()