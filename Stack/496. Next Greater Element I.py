class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        x=nums1
        y=nums2
        flag=0
        
        for i in x:
            flag=0
            for j in range(y.index(i),len(y)):
                    if i<y[j]:
                        stack.append(y[j])
                        flag=1
                        break
            if flag!=1:
                stack.append(-1)
        return stack
                    