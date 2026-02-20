#generate python code Different Approaches to String Reversal
def reverse_string_slicing(s):
    """Reverse a string using slicing."""
    return s[::-1]

def reverse_string_loop(s):
    """Reverse a string using a loop."""
    reversed_str = ''
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

def reverse_string_recursion(s):
    """Reverse a string using recursion."""
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverse_string_recursion(s[:-1])

def reverse_string_builtin(s):
    """Reverse a string using built-in functions."""
    return ''.join(reversed(s))

# Example usage
if __name__ == "__main__":
    test_string = "Hello, World!"
    print("Original String:", test_string)
    print("Reversed (Slicing):", reverse_string_slicing(test_string))
    print("Reversed (Loop):", reverse_string_loop(test_string))
    print("Reversed (Recursion):", reverse_string_recursion(test_string))
    print("Reversed (Built-in):", reverse_string_builtin(test_string))