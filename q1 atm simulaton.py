#let us assume that there is a single customer and there is 10000 balance in the account
# customerBalance will store the bank balance of the customer


"""printOperationsis used to print all the operations that the atm can perform"""
def printOperations():
    print("Choose the operation you want to use:")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. WithDraw Money")
    print("4. Exit")

#getOperation takes the customers input that is used to choose the operation required
def getOperation():
    return int(input("Enter option: "))

#doBalanceCheck will display the balance that the customer has
def doBalanceCheck(customerBalance):
    print("Current Balance is: "+ str(customerBalance))


#deposit will take the amount that is given and adds it to the customers account
def deposit(customerBalance):
    depositValue = int(input("Enter the amount deposited: "))
    return customerBalance+depositValue



#withdrawAmount will withdraw the amount if it is available or it will say not enough
def withdrawAmount(customerBalance):
    withdrawValue = int(input("Enter the amount to withdraw: "))
    if(customerBalance < withdrawValue):
        print("Not enough available in account")
        return customerBalance
    else:
        return customerBalance-withdrawValue

#performOperations will perform the operation that is chosen by the customer
def performOperations(operation,customerBalance):
    if operation==1:
        doBalanceCheck(customerBalance)
        print("Balance check successful.")
    elif operation==2:
        return deposit(customerBalance)
        print("Deposit taken and account updated.")
    elif operation==3:
        return withdrawAmount(customerBalance)
        print("Withdrawed X amount sucessfully.")
    else:
        print("Inalid Input, please try again.")

    
#main block that calls all functions that will help the atm simulator to run in order
if __name__=="__main__":
    customerBalance=10000
    while(1):
        printOperations()
        operation=getOperation()
        if operation == 4:
            break
        customerBalance=performOperations(operation, customerBalance)
        