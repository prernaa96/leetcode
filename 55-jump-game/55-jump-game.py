class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        if len(nums) == 1:
            return True
        
        i=0
        j=0
        
        while i != (len(nums)-1):
            # print(i,j)
            if i<=j:
                j = max(j,i+nums[i])
                if j>=(len(nums)-1):
                    return True 
                i+=1
            else:    
                return False    
            