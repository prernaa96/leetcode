class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        
        add=0
        minval=0
        for i in range(len(nums)):
            add+=nums[i]
            minval=min(add,minval)
        return -minval+1