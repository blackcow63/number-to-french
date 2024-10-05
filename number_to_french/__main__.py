import sys
import ast  # To safely evaluate a string as a Python literal
from .converter import NumberToFrench

def main():
    if len(sys.argv) > 1:
        try:
            # Extract the input argument, which should be a list in string format
            input_list_str = sys.argv[1]
            
            # Safely evaluate the string to a Python list using ast.literal_eval
            numbers = ast.literal_eval(input_list_str)
            
            # Ensure the evaluated result is a list of integers
            if not isinstance(numbers, list) or not all(isinstance(num, int) for num in numbers):
                raise ValueError("Input should be a list of integers.")
            
            # Create the NumberToFrench instance and convert the list of numbers
            converter = NumberToFrench()
            results = converter.convert_list_to_french(numbers)
            
            # Format the results as a JSON-like list of strings
            print(results)  # This will print the list directly
            
        except (ValueError, SyntaxError) as e:
            print(f"Error: {e}. Please provide a valid list of integers in the format: [1, 2, 3].")
    else:
        print("Usage: python -m number_to_french '[1, 2, 3]'")

if __name__ == "__main__":
    main()
