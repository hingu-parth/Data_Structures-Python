class Solution:
    def removeDuplicates(self, S: str) -> str:
        s=list(S)
        stack=[]
        for i in s:
            if stack==[]:
                stack.append(i)   
            elif i == stack[len(stack)-1]:
                stack.pop()
            else:
                stack.append(i)
        return ''.join(stack)
                