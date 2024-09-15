## problem :  remove duplicates from a sorted linked list

# Node class to represent each node of the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to remove duplicates from a sorted linked list
def remove_duplicates(head):
    current = head
    
    # Traverse the list till the last node
    while current is not None and current.next is not None:
        # Compare current node with the next node
        if current.data == current.next.data:
            # Skip the duplicate node
            current.next = current.next.next
        else:
            # Move to the next node if no duplicate
            current = current.next
    
    return head