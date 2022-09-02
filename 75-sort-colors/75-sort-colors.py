class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        count = [0]*3
        arr=[0]*len(nums)
        for i in range(len(nums)):
            count[nums[i]] = count[nums[i]]+1
        for i in range(1,len(count)):
            count[i] = count[i]+count[i-1]
        for i in range(len(nums)):
            arr[count[nums[i]]-1] = nums[i]
            count[nums[i]] -= 1
        for i in range(len(nums)):
            nums[i] = arr[i]
        return nums    
           