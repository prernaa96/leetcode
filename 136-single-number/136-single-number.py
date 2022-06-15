class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        flag = False
        
        if len(nums) == 1:
            return nums[0]
        
        
        for i in nums:
            if nums.count(i) == 1:
                return i
                
                
          