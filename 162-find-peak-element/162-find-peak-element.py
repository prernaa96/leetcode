class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        max_num= -2**31 - 1
        
        for i in range(len(nums)):
            j=i+1
            # print(i,j)
            max_num = max(max_num, nums[i])
            if j>len(nums)-1 or nums[j] < max_num:
                return i