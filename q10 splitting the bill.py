#the getInput gets the total bill, numbr of people and hte tip percent
def getInput():
    total=int(input("Enter the total amount: "))
    people=int(input("Enter the total number of people: "))
    tip=int(input("Enter the tip percentage: "))
    return total,people,tip

#totalAmount will calculate the total tip amount and return the total bill with tip
def totalAmount(total,tip):
    tipAmount=(tip*total)/100
    return total+tipAmount

#the bill amount is divided by the total number of people and split evenly
def splitting(total, people):
    return total/people

# main function calls the input, bill amount and perhead cost then prints the result
def main():
    total,people,tip = getInput()
    totalBill = totalAmount(total,tip)
    perCost = splitting(totalBill,people)
    print(totalBill," is the total amount added with the tip")
    print(perCost," is the cost each person must pay")

main()