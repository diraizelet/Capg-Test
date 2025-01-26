#takes the input from the user
def getInput():
    rows = int(input("Enter the string: "))
    order = input("Enter the Order 0-normal, 1 is reversed")
    return rows, order

#printPyramid prints the pyramid of the size specified in the rows and as normal or reversed
def printPyramid(rows, order):
    if order == "0":
        for i in range(0,rows+1):
            for j in range(i):
                print("*",end="")
            print("")
    else:
        while rows!=0:
            j=rows
            while j!=0:
                print("*",end="")
                j-=1
            print("")
            rows-=1


#calls the get input function and print pyramid function
def main():
    rows,order=getInput()
    printPyramid(rows,order)


main()