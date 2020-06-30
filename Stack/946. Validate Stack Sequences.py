class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack=[]
        for i in pushed:
            stack.append(i)
            if len(popped)==0: break
            while len(stack)!=0 and stack[-1]==popped[0]:
                s=stack.pop()
                popped.remove(s)
        return True if len(popped)==0 else False
        
        
        
        
                
                
                
        