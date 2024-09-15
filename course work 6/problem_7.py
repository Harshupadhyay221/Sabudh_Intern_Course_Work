## problem : Find the second last element from the linked list 

# Node class to represent each node of the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to find the second last element of the linked list
def find_second_last(head):
    # If the list has less than two elements
    if head is None or head.next is None:
        print("The list has fewer than two elements.")
        return None
    
    # Initialize two pointers
    second_last = None
    current = head
    
    # Traverse the list until we reach the last node
    while current.next is not None:
        second_last = current  # Keep track of the second last node
        current = current.next
    
    return second_last.data  # Return the second last element