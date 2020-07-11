class Solution(object):
    def peakIndexInMountainArray(self, A):
        
        lo, hi = 0, len(A) - 1
        peak=0
        while lo <= hi:
            mi = int(lo + (hi - lo) / 2)
            if A[mi-1] < A[mi] > A[mi + 1]:
                peak=mi
                return peak
            elif A[mi-1] < A[mi] < A[mi + 1]:
                lo=mi+1
            else:
                hi=mi-1
        return peak 