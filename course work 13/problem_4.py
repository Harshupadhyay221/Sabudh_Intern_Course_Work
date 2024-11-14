class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

def are_mirrors(root1, root2):
    # If both trees are empty, they are mirrors
    if root1 is None and root2 is None:
        return True

    # If one of them is empty but the other is not, they are not mirrors
    if root1 is None or root2 is None:
        return False

    # Check if the data of both roots is the same
 
    return (root1.data == root2.data and
            are_mirrors(root1.left, root2.right) and
            are_mirrors(root1.right, root2.left))