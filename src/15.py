import math

def find_sum_of_odd_and_even(num):
    odd_sum = 0
    even_sum = 0
    while num > 0:
        if (num % 2 == 1): 
            odd_sum += num
        else:
            even_sum += num
        num //= 2
    return odd_sum, even_sum

# Example usage
number = int(input("Enter a number: "))
result_odd_even = find_sum_of_odd_and_even(number)
print(f"Odd sum is {result_odd_even[0]}, Even sum is {result_odd_even[1]}")
