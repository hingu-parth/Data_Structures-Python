class Solution:
    def isValid(self, s: str) -> bool:
        s=list(s)
        stack=[]

        for i in s:
            if not stack:
                stack.append(i)
                
            elif (stack[len(stack)-1]=='(' and i==')') or (stack[len(stack)-1]=='[' and i==']') or (stack[len(stack)-1]=='{' and i=='}'):
                stack.pop()
            
            elif (stack[len(stack)-1]=='(' and (i=='(' or i=='[' or i=='{' or i==')' or i==']' or i=='}')) or (stack[len(stack)-1]=='[' and (i=='(' or i=='[' or i=='{' or i==')' or i==']' or i=='}')) or (stack[len(stack)-1]=='{' and (i=='(' or i=='[' or i=='{' or i==')' or i==']' or i=='}')):
                stack.append(i)
        print(s,stack)
                

        if not stack:   
             return 'true'            
        
                  