class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

def max_depth(root):
    # Base case: If the tree is empty, the depth is 0
    if root is None:
        return 0
    
    # Recursively find the depth of left and right subtrees
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)
    
    # The depth of the current node is 1 + maximum of left or right subtree depth
    return 1 + max(left_depth, right_depth)