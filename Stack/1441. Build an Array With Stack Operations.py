class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        new=[]
        for i in range(1,n+1):
            if i <= target[len(target)-1]:
                if i not in target:
                    new.append('Push')
                    new.append('Pop')
                else:
                    new.append('Push')
        return new
                
        