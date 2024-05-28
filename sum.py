# Simple Python program to calculate the sum of elements in a list

def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def main():
    # Define a list of numbers
    numbers = [1, 2, 3, 4, 5]

    # Calculate the sum of the numbers
    result = calculate_sum(numbers)

    # Print the result
    print("The sum of the numbers is:", result)

if __name__ == "__main__":
    main()
