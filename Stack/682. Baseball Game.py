class Solution:
    def calPoints(self, ops: List[str]) -> int:
        points=[]
        sum=[]
        for i in ops:
            if not points:
                print(points,sum)
                points.append(i)
                sum.append(i)
                print(points,sum)
            elif i=='C':
                points.pop()
                sum.pop()
            elif i=='D':
                points.append(2*(int(points[len(points)-1])))
                sum.append(int(points[len(points)-1])+int(sum[len(sum)-1]))
            elif i=='+':
                points.append(int(points[len(points)-1])+int(points[len(points)-2]))
                sum.append(int(points[len(points)-1])+int(sum[len(sum)-1]))
            else:
                points.append(i)
                sum_up=int(points[len(points)-1])+int(sum[len(sum)-1])
                
                sum.append(sum_up)
            
        return sum[len(sum)-1]
                
                
        