#generate a python code for even numbers using function  that should handle zero and negative even number should satisfies the even number and negative numbers as well
def is_even(num):
    if num % 2 == 0:
        if num < 0:
            return "Negative Even"
        elif num == 0:
            return "Zero"
        else:
            return "Positive Even"
    else:
        return "Not an Even Number"
# Testing
print(is_even(10))   # Positive Even
print(is_even(-4))   # Negative Even
print(is_even(0))    # Zero

print(is_even(7))    # Not an Even Number

#genearte a asseration  for above code
assert is_even(10) == "Positive Even", "Test case 1 failed"
assert is_even(-4) == "Negative Even", "Test case 2 failed" 
assert is_even(0) == "Zero", "Test case 3 failed"
assert is_even(7) == "Not an Even Number", "Test case 4 failed"

print("All test cases passed!")

#genearte a unit   for above code 
import unittest
class TestIsEven(unittest.TestCase):
    def test_positive_even(self):
        self.assertEqual(is_even(10), "Positive Even")
        
    def test_negative_even(self):
        self.assertEqual(is_even(-4), "Negative Even")
        
    def test_zero(self):
        self.assertEqual(is_even(0), "Zero")
        
    def test_not_even(self):
        self.assertEqual(is_even(7), "Not an Even Number")
if __name__ == '__main__':
    unittest.main()
#genearte a PYTEST   for above code 
import pytest
def test_is_even():
    assert is_even(10) == "Positive Even"
    assert is_even(-4) == "Negative Even"
    assert is_even(0) == "Zero"
    assert is_even(7) == "Not an Even Number"
if __name__ == "__main__":
    pytest.main()
    
    

        

    
    
    
    
