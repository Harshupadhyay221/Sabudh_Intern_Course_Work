class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

def find_height(root):
    # Base case: If the tree is empty, return 0
    if root is None:
        return 0
    
    # Recursively find the height of left and right subtrees
    left_height = find_height(root.left)
    right_height = find_height(root.right)
    
    # The height of the current node is 1 + the maximum height of its left or right subtrees
    return 1 + max(left_height, right_height)