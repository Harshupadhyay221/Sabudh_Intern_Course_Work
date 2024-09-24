# 1.Inserting at the Beginning

# Definition for a node in the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to insert a node at the beginning of the linked list
def insert_at_head(head, value):
    # Create a new node with the given value
    new_node = Node(value)
    # Point the new node's next to the current head
    new_node.next = head
    # Update the head to the new node
    return new_node