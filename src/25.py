def multiply_numbers(x, y):
    """
    Multiplies two numbers and returns the result.
    
    Args:
    x (int): The first number to be multiplied.
    y (int): The second number to be multiplied.
    
    Returns:
    int: The product of x and y.
    """
    return x * y

def main():
    # Example usage
    num1 = 5
    num2 = 3
    result = multiply_numbers(num1, num2)
    print(f"The product of {num1} and {num2} is: {result}")

if __name__ == "__main__":
    main()
