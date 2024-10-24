class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        # Initialize a TreeNode with a value and optional left and right children
        self.val = val
        self.left = left
        self.right = right

def is_valid_bst(root):
    # Helper function to validate the BST properties
    def validate(node, low=float('-inf'), high=float('inf')):
        # If the node is None, we have reached a leaf node, which is valid
        if not node:
            return True
        # Check if the current node's value is within the valid range
        if not (low < node.val < high):
            return False
        # Recursively validate the left and right subtrees
        return (validate(node.left, low, node.val) and  # Left subtree must have values < current node's value
                validate(node.right, node.val, high))  # Right subtree must have values > current node's value

    # Start the validation process from the root
    return validate(root)

# Default Input
root = TreeNode(2)  # Create the root node with value 2
root.left = TreeNode(1)  # Create the left child with value 1
root.right = TreeNode(3)  # Create the right child with value 3

# Check if the tree is a valid BST
result = is_valid_bst(root)
print(f"Is the tree a valid BST? {result}")
