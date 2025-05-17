def calculate_average(numbers):
    # Missing type hints
    # Missing docstring
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)

def process_data(data):
    # Unused import
    import json
    # Undefined variable
    result = []
    for item in data:
        processed = item * 2
        result.append(processed)
    return result

# Missing main guard
print("Testing functions...")
test_numbers = [1, 2, 3, 4, 5]
average = calculate_average(test_numbers)
print(f"Average: {average}")

# Inconsistent string quotes
print("Testing process_data...")
test_data = [1, 2, 3]
processed = process_data(test_data)
print(f"Processed: {processed}") 