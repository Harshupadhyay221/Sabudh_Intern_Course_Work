# 2.Maximum Twin Sum of A Linked List

# Node class for the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to reverse a linked list
def reverse_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# Function to find the maximum twin sum
def maximum_twin_sum(head):
    if not head or not head.next:
        return 0

    # Find the middle of the linked list using the slow and fast pointers
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse the second half of the linked list
    second_half = reverse_list(slow)

    # Calculate the maximum twin sum
    max_sum = 0
    first_half = head

    while second_half:
        # Calculate twin sum
        current_sum = first_half.data + second_half.data
        max_sum = max(max_sum, current_sum)
        
        # Move to the next node in both halves
        first_half = first_half.next
        second_half = second_half.next

    return max_sum
