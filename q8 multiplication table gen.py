
# table_generator will  multiply and display the tables till where it is needed
def table_generator(tillNum,num):
    for i in range(1, tillNum+1):
        print(f"{num} x {i} = {num * i}")
        

# main function will take all inputs and call the table generating fucntion
def main():
    num = int(input("Enter the Number whose tables are needed: "))
    tillNum = int(input("Enter the range needed: "))

    if num==0:
        print("All multiples of 0 are always 0.")
    else:
        print("Here are the tables")
        table_generator(tillNum,num)


if __name__ =="__main__":
    main()