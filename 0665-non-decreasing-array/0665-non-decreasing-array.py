class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        
        
    
    # [1,7,5,4]
    # -6,2,1
    # [1,2,5,4]
    # -1,-3,1
    # [5,2,7,6,7]
    # -1,-5,1,-1
        
        c=0
        diff=0
        for i in range(len(nums)-1):
            if nums[i] > nums[i + 1]:
                if c>0:
                    return False
                c+=1
            if 0<i < len(nums) - 2 and nums[i - 1] > nums[i + 1] and nums[i] > nums[i + 2]:
                    return False
        
        return True
        
    
    
    