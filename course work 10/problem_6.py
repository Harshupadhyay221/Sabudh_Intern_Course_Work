


def follows_pattern_order(string, pattern):
    # Initialize a map to store the index of each pattern character in the string
    last_seen = {char: -1 for char in pattern}
    
    # Variable to track the position of the last seen pattern character
    last_position = -1
    
    # Traverse the string
    for i, char in enumerate(string):
        # If the character is in the pattern
        if char in last_seen:
            # Check if it follows the order
            if last_seen[char] < last_position:
                return False
            # Update the last position and last_seen index for the current pattern character
            last_seen[char] = i
            last_position = i
    
    return True