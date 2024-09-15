## Delete Middle of Linked List 

# Node class to represent each node of the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to delete the middle node of the linked list
def delete_middle(head):
    if head is None or head.next is None:
        # If the list is empty or contains only one element, return None
        return None

    slow = head
    fast = head
    prev = None  # To keep track of the node before slow

    # Move fast by two and slow by one
    while fast is not None and fast.next is not None:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    # Delete the middle node by skipping it
    prev.next = slow.next

    return head