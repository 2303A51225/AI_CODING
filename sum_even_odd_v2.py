def calculate_sums(numbers):
    """
    Calculate the sum of even numbers and the sum of odd numbers separately.
    Uses list comprehensions for a more Pythonic approach.
    
    Args:
        numbers: A list of numbers
        
    Returns:
        A tuple containing (sum_of_evens, sum_of_odds)
    """
    sum_even = sum(num for num in numbers if num % 2 == 0)
    sum_odd = sum(num for num in numbers if num % 2 != 0)
    
    return sum_even, sum_odd


def calculate_sums_alternative(numbers):
    """
    Alternative implementation using filter function.
    
    Args:
        numbers: A list of numbers
        
    Returns:
        A tuple containing (sum_of_evens, sum_of_odds)
    """
    sum_even = sum(filter(lambda x: x % 2 == 0, numbers))
    sum_odd = sum(filter(lambda x: x % 2 != 0, numbers))
    
    return sum_even, sum_odd


def main():
    # Example usage
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Using list comprehension approach
    sum_even, sum_odd = calculate_sums(numbers)
    
    print(f"List of numbers: {numbers}")
    print(f"Sum of even numbers: {sum_even}")
    print(f"Sum of odd numbers: {sum_odd}")
    print()
    
    # Using filter approach
    sum_even2, sum_odd2 = calculate_sums_alternative(numbers)
    print(f"Alternative method - Sum of even numbers: {sum_even2}")
    print(f"Alternative method - Sum of odd numbers: {sum_odd2}")


if __name__ == "__main__":
    main()
