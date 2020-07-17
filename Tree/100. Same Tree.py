# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        flag=0
        def issametree(p,q,flag):
            if (p and not q) or (not p and q):
                flag=1
                return flag
            elif not p and not q:
                return flag
            if p.val==q.val:
                # print(p.val,q.val)
                flag=issametree(p.left,q.left,flag)
                flag=issametree(p.right,q.right,flag)

            else:
                # print(p.val,q.val)
                flag=1
                return flag
            
            if flag==1:
                return flag
            else:
                # print(flag)
                return flag
                
         
        flag=issametree(p,q,flag)
        print(flag)
        if flag==1:
            return False
        elif flag==0:
            return True
        
        
        
            
        