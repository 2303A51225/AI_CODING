def calculate_sums(numbers):
    """
    Calculate the sum of even numbers and the sum of odd numbers separately.
    
    Args:
        numbers: A list of numbers
        
    Returns:
        A tuple containing (sum_of_evens, sum_of_odds)
    """
    sum_even = 0
    sum_odd = 0
    
    for num in numbers:
        if num % 2 == 0:
            sum_even += num
        else:
            sum_odd += num
    
    return sum_even, sum_odd


def main():
    # Example usage
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    sum_even, sum_odd = calculate_sums(numbers)
    
    print(f"List of numbers: {numbers}")
    print(f"Sum of even numbers: {sum_even}")
    print(f"Sum of odd numbers: {sum_odd}")


if __name__ == "__main__":
    main()
