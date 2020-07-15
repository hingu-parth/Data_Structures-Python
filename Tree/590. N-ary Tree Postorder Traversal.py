"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
Solution 1: Recursive
        stack=[]
        if not root:
            return []
        else:
            for i in root.children:
                stack+=self.postorder(i)
            stack.append(root.val)
        return stack
    
Solution 2: Iterative
        if not root:
            return []
        
        main=[]
        stack=[root]
        while stack:
            cur=stack.pop()
            main.append(cur.val)
            stack.extend(cur.children)
        return reversed(main)
                
            
    
        