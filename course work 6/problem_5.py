## Problem : add 1 to the linkedlist

# Node class to represent each node of the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to reverse the linked list
def reverse_linked_list(head):
    prev = None
    current = head
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# Function to add 1 to the number represented by the linked list
def add_one(head):
    # Step 1: Reverse the linked list
    head = reverse_linked_list(head)
    
    # Step 2: Add 1 to the first node
    current = head
    carry = 1
    
    while current is not None:
        current.data += carry
        carry = current.data // 10  # Carry will be 1 if the sum is 10 or more
        current.data = current.data % 10  # Keep the last digit in the node
        
        # Move to the next node
        if current.next is None and carry > 0:
            # If carry remains and it's the last node, add a new node
            current.next = Node(carry)
            carry = 0
        
        current = current.next
    
    # Step 3: Reverse the list back to its original order
    head = reverse_linked_list(head)
    
    return head