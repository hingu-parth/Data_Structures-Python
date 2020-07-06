class Solution:
    def reverseParentheses(self, s: str) -> str:
        s=list(s)
        temp=[]
        j=0
        
        stack=[]
        while j<len(s): 
            if s[j]==')':
                for i in reversed(stack):
                    if i!='(':
                        temp.append(i)
                        stack.pop()
                        # print(temp,'t')
                    elif i=='(':
                        stack.pop()
                        break
                   
                stack=stack+temp
                temp.clear()
            else:
                stack.append(s[j])
                print(stack)
            j+=1
        
        return ''.join(stack)
                    
                        