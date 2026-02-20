#generate python code for palidrome checking
def is_palindrome(s):    
    """Check if a string is a palindrome."""
    cleaned_str = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned_str == cleaned_str[::-1] 

# Example usage
if __name__ == "__main__":
    test_strings = ["A man, a plan, a canal: Panama", "racecar", "hello", "No 'x' in Nixon"]
    for s in test_strings:  
        result = is_palindrome(s)
        print(f'"{s}" is a palindrome: {result}')
        
