class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s=list(S)
        t=list(T)
        stack1=[]
        stack2=[]
        flag=0
        for i in s:
            if i!='#':
                stack1.append(i)
            elif not stack1 and i=='#':
                continue
            elif i=='#':
                stack1.pop()
        for i in t:
            if i!='#':
                stack2.append(i)
            elif not stack2 and i=='#':
                continue
            elif i=='#':
                stack2.pop()
        
        print(stack1,stack2)
        if stack1 == stack2:
            return True
        else:
            return False