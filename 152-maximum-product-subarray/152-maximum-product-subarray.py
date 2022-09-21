class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        if len(nums)==1:
            return nums[0]
        
        gmax = pmax = pmin = nums[0]
        
        for i in range(1,len(nums)):
            
            cmax = max(pmax*nums[i], pmin*nums[i], nums[i])
            cmin = min(pmax*nums[i], pmin*nums[i], nums[i])
            
            gmax = max(gmax, cmax)
            
            pmax,pmin = cmax,cmin
            
        return gmax    
            