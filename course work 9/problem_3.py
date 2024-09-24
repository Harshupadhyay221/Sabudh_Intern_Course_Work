# 3 remove duplicates 

def remove_duplicates(s):
    stack = []
    
    # Traverse each character in the string
    for char in s:
        # If stack is non-empty and the top of the stack equals the current character
        if stack and stack[-1] == char:
            stack.pop()  
        else:
            stack.append(char) 
    
    # Return the final string by joining the elements in the stack
    return ''.join(stack)