class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

def are_identical(root1, root2):
    # If both trees are empty, they are identical
    if root1 is None and root2 is None:
        return True
    
    # If one tree is empty and the other is not, they are not identical
    if root1 is None or root2 is None:
        return False
    
    # Check if the data of the current nodes is the same
    # And check recursively for left and right subtrees
    return (root1.data == root2.data and 
            are_identical(root1.left, root2.left) and
            are_identical(root1.right, root2.right))