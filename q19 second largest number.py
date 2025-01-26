def get_numbers():
    """
    Function to take input from the user and return a list of numbers.
    """
    numbers = input("Enter numbers separated by spaces: ")
    return list(map(int, numbers.split()))

def find_second_largest(numbers):
    """
    Function to find the second largest number in a list.
    """
    if len(numbers) < 2:
        return None  # Not enough elements to find the second largest

    first = second = float('-inf')
    for number in numbers:
        if number > first:
            second = first
            first = number
        elif first > number > second:
            second = number

    return second

def main():
    """
    Main function to execute the program.
    """
    numbers = get_numbers()
    second_largest = find_second_largest(numbers)
    if second_largest is None:
        print("Not enough elements to find the second largest number.")
    else:
        print(f"The second largest number is: {second_largest}")

if __name__ == "__main__":
    main()