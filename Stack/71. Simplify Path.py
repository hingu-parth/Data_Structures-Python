class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        p=path.split('/')
        print(p)
        
        for i in p:
            # if i=='':
            #     p.pop(p.index(i))
                
            if i!='.' and i!='..' and i!='':
                stack.append(i)
            elif i=='..' and stack:
                stack.pop()
                
                
            print(stack)
            
            
        return '/'+'/'.join(stack)
            
            
        