class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        setnum = set(nums)
        lennum = len(setnum)
        
        if len(nums) == 1:
            return 1
        
        i=0
        while i < len(nums):
            if i+1 <= len(nums):
                if nums[i] == nums[i+1]:
                    del nums[i]
                    i=0
                else:
                    i+=1 
            
            if lennum == len(nums):
                break
                
                return len(nums)  