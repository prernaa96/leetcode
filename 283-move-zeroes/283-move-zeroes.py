class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        
        # if len(nums) == 1:
        #     return nums
        
        c = nums.count(0)
        # if c == len(nums):
        #     return nums
        
        for i in range(c):
            if 0 in nums:
                nums.append(nums.pop(nums.index(0)))  
        # print(nums)    
        
        
      
        