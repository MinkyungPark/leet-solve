# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# [3, 9, 20, None, None, 15, 7]
# node3 = TreeNode(3)
# node9 = TreeNode(9)
# node20 = TreeNode(20)
# node15 = TreeNode(15)
# node7 = TreeNode(7)

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))