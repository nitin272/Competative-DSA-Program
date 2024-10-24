class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        # Initialize a TreeNode with a value and optional left and right children
        self.val = val
        self.left = left
        self.right = right

def lowest_common_ancestor(root, p, q):
    # Base case: if the root is None or matches either p or q, return root
    if not root or root == p or root == q:
        return root

    # Recur on the left and right subtrees
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    # If both left and right returned non-null values, this root is the LCA
    if left and right:
        return root

    # Otherwise, return the non-null child (either left or right)
    return left if left else right

# Default Input
root = TreeNode(3)  # Create the root node with value 3
root.left = TreeNode(5)  # Create left child with value 5
root.right = TreeNode(1)  # Create right child with value 1
root.left.left = TreeNode(6)  # Create left child of 5 with value 6
root.left.right = TreeNode(2)  # Create right child of 5 with value 2
root.right.left = TreeNode(0)  # Create left child of 1 with value 0
root.right.right = TreeNode(8)  # Create right child of 1 with value 8

# Define nodes for which to find the LCA
p = root.left  # Node with value 5
q = root.left.right  # Node with value 2

# Find the lowest common ancestor of nodes p and q
result = lowest_common_ancestor(root, p, q)
print(f"Lowest Common Ancestor of {p.val} and {q.val} is: {result.val}")
