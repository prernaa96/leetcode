class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        c=0
        arr=[0]*60
        for i in range(len(time)):
            a=time[i]%60
            c+=arr[(60 - a)%60]
            arr[a]+=1
        return c
        
        
        
            