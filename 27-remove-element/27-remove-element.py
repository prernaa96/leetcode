class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        c=0
        i=0
        
        if val not in nums:
            return len(nums)
        
        if len(nums) == 1:
            return 0
        
        while i < len(nums)-1:
            if nums[i] == val:
                if nums[i] == nums[len(nums)-1-c]:
                    c+=1
                else:
                    nums[i], nums[len(nums)-1-c] = nums[len(nums)-1-c], nums[i] 
                    i+=1
            else:
                i+=1
                
            count = nums.count(val)
            diff = len(nums) - count

            if diff == 0:
                return 0

            if  i == diff:
                return diff
                     