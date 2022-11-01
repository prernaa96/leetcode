class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
       
        maxval=-1000000
        sums=0
        
        for i in nums:
            sums+=i
            maxval=max(maxval, sums)
            
            if sums<0:
                sums=0
                
            # print(maxval,sums)
        return maxval
    
        