from typing import List, Union
import json
from statistics import mean

def calculate_average(numbers: List[Union[int, float]]) -> float:
    """
    Calculate the average of a list of numbers.
    
    Args:
        numbers (List[Union[int, float]]): A list of numbers to calculate average from
        
    Returns:
        float: The average of the numbers
        
    Raises:
        ValueError: If the input list is empty
        TypeError: If the input contains non-numeric values
    """
    if not numbers:
        raise ValueError("Cannot calculate average of an empty list")
    
    try:
        return mean(numbers)
    except TypeError as e:
        raise TypeError("All elements must be numbers") from e

def process_data(data: List[int]) -> List[int]:
    """
    Process a list of integers by doubling each value.
    
    Args:
        data (List[int]): A list of integers to process
        
    Returns:
        List[int]: A new list containing doubled values
        
    Raises:
        TypeError: If the input contains non-integer values
    """
    if not all(isinstance(x, int) for x in data):
        raise TypeError("All elements must be integers")
    
    return [item * 2 for item in data]

def main() -> None:
    """Main function to demonstrate the usage of other functions."""
    try:
        # Test calculate_average
        print("Testing calculate_average...")
        test_numbers = [1, 2, 3, 4, 5]
        average = calculate_average(test_numbers)
        print(f"Average: {average}")
        
        # Test process_data
        print("\nTesting process_data...")
        test_data = [1, 2, 3]
        processed = process_data(test_data)
        print(f"Processed: {processed}")
        
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main() 