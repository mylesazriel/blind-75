# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Recursive, depth first search
        if root is None:  # Case when you hit the bottom of the tree
            return None

        self.invertTree(root.left)
        self.invertTree(root.right)

        # Postorder traversal
        temp = root.left
        root.left = root.right
        root.right = temp

        return root
