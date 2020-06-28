class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        l = list(s)
        i = 0
        while i < len(l):
            if not stack and l[i] == ')':
                l.pop(i)
                continue
            elif l[i] == '(':
                stack.append(i)
            elif l[i] == ')' and l[stack[-1]] == '(':
                stack.pop()
            i += 1
        if stack:
            x = len(stack)-1
            while x >= 0:
                l.pop(stack[x])
                stack.pop()
                x-=1      
        return ''.join(l)

# whenever you are adding or removing from the list which is on loop, always use while loop