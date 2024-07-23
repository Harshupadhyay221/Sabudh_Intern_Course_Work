## Problem 2
#You have been given a string. You need to remove all the duplicates from the string. The final output string should contain each character only once. The respective order of the characters inside the string should remain the same. You can traverse the string only once.


def remove_duplicates(input_string):
    seen = set()         # Set to track seen characters
    result = []          # List to build the output string
    
    for char in input_string:
        if char not in seen:
            seen.add(char)
            result.append(char)
    
    return ''.join(result)  # Join the list into a string

# Example usage
input_string = input("Enter a string: ")
output_string = remove_duplicates(input_string)
print(f"Output: {output_string}")

# aproach
# 1. create a set to track seen characters
# 2. create a list to build the output string
# 3. iterate through the input string
# 4. if the current character is not in the set, add it to the set and
# 5. append the character to the output list
