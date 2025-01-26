#getInput get the data from the user
def getInput(data):
    name=int(input("Enter the size of list "))
    for i in range(name):
        name=int(input("Enter the data: "))
        data.append(name)
    return data


# segregates the odd and even numbers and stores them in seperate lists
def oddEvenSeperator(data):
    odd=[]
    even=[]
    for x in data:
        if x%2 ==0:
            even.append(x)
        else:
            odd.append(x)
    return odd,even


def main():
    data=[]
    data=getInput(data)
    odd,even= oddEvenSeperator(data)
    print("Odd: ", odd)
    print("Even: ", even)

main()
