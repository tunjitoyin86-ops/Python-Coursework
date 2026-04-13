import pytest  # pyright: ignore[reportMissingImports]
from src.factorial import factorial 

def test_factorial_basic(): 
    assert factorial(5) == 120 
    assert factorial(3) == 6 
 
def test_factorial_zero_and_one(): 
    assert factorial(0) == 1 
    assert factorial(1) == 1 
 
def test_factorial_negative_error(): 
    # This checks that the function correctly raises an error for bad input 
    with pytest.raises(ValueError): 
        factorial(-1)  