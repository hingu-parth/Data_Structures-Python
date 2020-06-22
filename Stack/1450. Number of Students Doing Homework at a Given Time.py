class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        counter=0
        for i,j in zip(startTime,endTime):
            if queryTime in range(i,j+1):
                counter+=1
        return counter