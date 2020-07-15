# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        
        a=[]
        def search(root,L,R,a):
            if root:
                search(root.left,L,R,a)
                if (root.val>=L) and (root.val<=R):
                    a.append(root.val)
                search(root.right,L,R,a)
            return sum(a)
        a=search(root,L,R,a)
        return a
        