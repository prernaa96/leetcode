class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        arr=[]
        tot=0
        for i in range(len(gain)):
            tot = tot+gain[i]
            arr.append(tot)
        
        maxval=max(arr)
        if maxval<=0:
            return 0
        return maxval
        
        