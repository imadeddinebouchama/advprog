def length(lst):
   
    return len(lst)

def mean(lst):
    
    if not lst:
        raise ValueError("Cannot calculate mean of empty list")
    
    
    for item in lst:
        if not isinstance(item, (int, float)):
            raise TypeError(f"List contains non-numeric value: {item}")
    
    return sum(lst) / len(lst)

def range_of_list(lst):
    """Calculate the range (max - min) of the list."""
    if not lst:
        raise ValueError("Cannot calculate range of empty list")
    
    # Verify all elements are numeric
    for item in lst:
        if not isinstance(item, (int, float)):
            raise TypeError(f"List contains non-numeric value: {item}")
    
    return max(lst) - min(lst)

# Test cases
def run_tests():
    # Test case 1: Empty list
    empty_list = []
    print("\nTest Case 1: Empty list")
    print(f"Length: {length(empty_list)}")
    try:
        print(f"Mean: {mean(empty_list)}")
    except ValueError as e:
        print(f"Mean error: {e}")
    try:
        print(f"Range: {range_of_list(empty_list)}")
    except ValueError as e:
        print(f"Range error: {e}")

    # Test case 2: Single element
    single_element = [5]
    print("\nTest Case 2: Single element")
    print(f"Length: {length(single_element)}")
    print(f"Mean: {mean(single_element)}")
    print(f"Range: {range_of_list(single_element)}")

    # Test case 3: Negative numbers
    negative_numbers = [-5, -3, -1, -10, -2]
    print("\nTest Case 3: Negative numbers")
    print(f"Length: {length(negative_numbers)}")
    print(f"Mean: {mean(negative_numbers)}")
    print(f"Range: {range_of_list(negative_numbers)}")

    # Test case 4: Floating-point numbers
    float_numbers = [1.5, 2.7, 3.2, 4.9, 5.1]
    print("\nTest Case 4: Floating-point numbers")
    print(f"Length: {length(float_numbers)}")
    print(f"Mean: {mean(float_numbers)}")
    print(f"Range: {range_of_list(float_numbers)}")

    # Test case 5: Non-numeric values
    invalid_list = [1, 2, "three", 4, 5]
    print("\nTest Case 5: Non-numeric values")
    print(f"Length: {length(invalid_list)}")
    try:
        print(f"Mean: {mean(invalid_list)}")
    except TypeError as e:
        print(f"Mean error: {e}")
    try:
        print(f"Range: {range_of_list(invalid_list)}")
    except TypeError as e:
        print(f"Range error: {e}")

if __name__ == "__main__":
    run_tests()