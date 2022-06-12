class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxval = -10001
        total = 0
        
        if len(nums) == 1:
            return nums[0]
        
        for i in nums:
            
            if total < 0:
                total = 0
                
            total = total + i
            
            if total > maxval:
                maxval = total
                
        # print(maxval)       
        
        return maxval
    
        