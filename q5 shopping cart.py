#the cart isa dictionary that can store the item name and its price by mapping 
#them together

#add_item will add the new item name and the price to the cart
def add_item(cart):
    item_name = input("Enter the item name: ")
    item_price = float(input("Enter the item price: "))
    cart.append({'name': item_name, 'price': item_price})
    print(f"{item_name} has been added to the cart.\n")


# view_cart will print all the items present in the cart
def view_cart(cart):
    if not cart:
        print("Your cart is empty.\n")
    else:
        print("Items in your cart:")
        for item in cart:
            print(f"{item['name']} - ${item['price']:.2f}")
        print()

#calculate_total will iterate through the cart[] and add all the values of the items
def calculate_total(cart):
    total = sum(item['price'] for item in cart)
    print(f"Total price of items in the cart: ${total:.2f}\n")


#in main the choices are given and we can choose 
#the if else statement will check and call the relevant fucntion
def main():
    cart = []
    while True:
        print("1. Add item")
        print("2. View cart")
        print("3. Calculate total")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_item(cart)
        elif choice == '2':
            view_cart(cart)
        elif choice == '3':
            calculate_total(cart)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()