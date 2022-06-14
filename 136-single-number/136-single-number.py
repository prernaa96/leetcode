class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        
        for i in nums:
            count = nums.count(i)
            if count == 1:
                return i