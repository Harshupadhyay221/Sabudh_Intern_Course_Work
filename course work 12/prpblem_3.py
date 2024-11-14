class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

# Helper function to calculate subtree sum and check for target sum
def check_subtree_sum(root, target_sum):
    # Base case: If the tree is empty, return 0
    if root is None:
        return 0
    
    # Recursively calculate the sum of left and right subtrees
    left_sum = check_subtree_sum(root.left, target_sum)
    right_sum = check_subtree_sum(root.right, target_sum)
    
    # Calculate the sum of the current subtree
    current_sum = root.data + left_sum + right_sum
    
    # If the sum of the current subtree equals the target sum, we set a flag
    if current_sum == target_sum:
        check_subtree_sum.is_found = True
    
    # Return the current subtree sum
    return current_sum
