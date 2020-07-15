"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
# Solution 1: Iterative
        if not root:
            return []
        traversal = []
        stack = [root]
        while stack:
            cur = stack.pop()
            traversal.append(cur.val)
            a=reversed(cur.children)
            stack.extend(a)
        return traversal
        
# Solution 2: Recursive
        stack=[]
        if not root:
            return []
        else:
            stack.append(root.val)
            for i in root.children:
                stack+=self.preorder(i)
            return stack
        
                