# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            ans.append(node.val)
            inorder(node.right)
        
        inorder(root)
        return ans

    def inorderTraversal_stack(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        
        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            res.append(root.val)
            root = root.right
        
        return res