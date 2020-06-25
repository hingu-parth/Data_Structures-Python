class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stack=[]
        list=''
        i=0
        while i<len(S):
            if S[i] =='(':
                stack.append(S[i])
            elif S[i] ==')':
                stack.pop()
            if not stack:
                list+=S[1:i]
                S=S[i+1:]
                i=0
            else:
                i+=1
        return list
      
                       
            
        