# problem : Add two numbers represented by Linked List 

# Node class to represent each node of the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to add two numbers represented by linked lists
def add_two_numbers(l1, l2):
    carry = 0
    dummy_node = Node(0)  # A dummy node to help build the result list
    current = dummy_node
    
    while l1 is not None or l2 is not None or carry > 0:
        # Extract values from the current nodes, or use 0 if one list is shorter
        val1 = l1.data if l1 is not None else 0
        val2 = l2.data if l2 is not None else 0
        
        # Calculate the sum and the carry
        total = val1 + val2 + carry
        carry = total // 10
        sum_digit = total % 10
        
        # Add the sum digit to the new linked list
        current.next = Node(sum_digit)
        current = current.next
        
        # Move to the next nodes
        if l1 is not None:
            l1 = l1.next
        if l2 is not None:
            l2 = l2.next
    
    # Return the next of the dummy node as the head of the result list
    return dummy_node.next