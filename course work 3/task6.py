def romanToInt(s):
    # Step 1: Create a mapping of Roman numerals to their values
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    # Initialize the total to 0
    total = 0
    
    #  Iterate through the string
    for i in range(len(s) - 1):
        # Get the value of the current symbol
        curr = roman[s[i]]
        # Get the value of the next symbol
        next = roman[s[i + 1]]
        
        # Compare the current value with the next value
        if curr < next:
            # Subtract current value if it's smaller
            total -= curr
        else:
            # Otherwise, add the current value
            total += curr
    
    #Add the value of the last symbol
    total += roman[s[-1]]
    
    return total