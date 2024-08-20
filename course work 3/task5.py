## Problem 5 : numeric to roman



def intToRoman(num):
    # List of tuples in the form (Roman numeral, integer value)
    roman = [
        ("M", 1000),
        ("CM", 900),
        ("D", 500),
        ("CD", 400),
        ("C", 100),
        ("XC", 90),
        ("L", 50),
        ("XL", 40),
        ("X", 10),
        ("IX", 9),
        ("V", 5),
        ("IV", 4),
        ("I", 1)
    ]
    
    # Initialize the result string
    result = ""
    
    # Iterate through the list of tuples
    for x, value in roman:
        # Append the Roman numeral and reduce the number
        while num >= value:
            result += x
            num -= value
    
    return result