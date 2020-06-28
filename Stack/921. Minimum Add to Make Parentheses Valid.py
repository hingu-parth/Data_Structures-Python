class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        S=list(S)
        if not S:
            return 0
        stack=[]
        for i in S:
            if not stack:
                stack.append(i)
            elif (stack[len(stack)-1]=='(' and i==')'):
                stack.pop()
            elif (i==stack[len(stack)-1]) or (i=='(' and stack[len(stack)-1]==')'):
                stack.append(i)
        return len(stack)
            
        