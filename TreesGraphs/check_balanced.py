def check_balanced(tree):
    # A function to check if a binary tree is balanced.
    # Time O(N), Space O(H), where N is the num of nodes in tree and H is the height of the tree.
    if not tree:
        return -1
    left_height = check_balanced(tree.left)
    if left_height == float('-inf'):
        return float('-inf')
    right_height = check_balanced(tree.right)
    if right_height == float('-inf'):
        return float('-inf')
    height_diff = left_height - right_height
    if abs(height_diff) > 1:
        return float('-inf')
    else:
        return max(left_height, right_height) + 1


class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


root = BinaryTreeNode(314)
root.left = BinaryTreeNode(6)
root.right = BinaryTreeNode(6)
root.left.left = BinaryTreeNode(271)
root.left.right = BinaryTreeNode(561)
root.right.left = BinaryTreeNode(2)
root.right.right = BinaryTreeNode(271)
root.left.left.left = BinaryTreeNode(28)
root.left.left.right = BinaryTreeNode(0)
root.left.right.right = BinaryTreeNode(3)
root.right.left.right = BinaryTreeNode(1)
root.right.right.right = BinaryTreeNode(28)

print(check_balanced(root))
