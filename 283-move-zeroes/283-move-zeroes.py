class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        for i in range(nums.count(0)):
            if 0 in nums:
                nums.append(nums.pop(nums.index(0)))    
        
        
      
        