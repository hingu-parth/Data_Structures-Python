# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def new(root,sumv):
            if not root:
                return sumv
            root.val+=new(root.right,sumv)
            print(root.val)
            return new(root.left,root.val)
        
        new(root,0)
        return root

        