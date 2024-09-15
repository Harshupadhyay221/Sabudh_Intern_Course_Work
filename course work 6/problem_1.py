## PROBLEM : Find middle of given linked list


# Node class to represent each node of the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to print the middle of the linked list
def print_middle(head):
    if head is None:
        return
    
    slow = head
    fast = head
    
    # Move fast by two and slow by one
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    
    # When fast reaches the end, slow will be at the middle
    print("The middle element is:", slow.data)


