## Problem : Reverse a linked list

# Node class to represent each node of the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to reverse the linked list
def reverse(head):
    prev = None  # Initialize previous to None
    current = head  # Start with the head as current
    
    while current is not None:
        next_node = current.next  # Store the next node
        current.next = prev  # Reverse the current node's pointer
        prev = current  # Move prev one step forward
        current = next_node  # Move current one step forward
    
    # At the end, prev will be the new head
    return prev
