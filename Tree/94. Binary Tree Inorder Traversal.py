# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:

#Solution 1:
        l = []
        def helper(root, l):
            if root:
                helper(root.left, l)
                l.append(root.val)
                helper(root.right, l)
            return l
        helper(root, l)
        return l
        
#Solution 2:
         if not root:
             return []
         else:
             return self.inorderTraversal(root.left)+[root.val]+self.inorderTraversal(root.right)
        