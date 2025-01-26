
def fizzbuzz():
# Loop through numbers from 1 to 100
    for i in range(1, 101,2):
# Check if the number is a multiple of both 3 and 5
        if i % 3 == 0 and i % 5 == 0:
            print(i," FizzBuzz")
                # Check if the number is a multiple of 3
        elif i % 3 == 0:
            print(i, " Fizz")
                # Check if the number is a multiple of 5
        elif i % 5 == 0:
            print(i, " Buzz")
                # If the number is not a multiple of 3 or 5, print the number
        

        # Call the fizzbuzz function
fizzbuzz()