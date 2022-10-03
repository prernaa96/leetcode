class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        
        window_sum = sum(nums[:k])
        maxval=window_sum
        
        for i in range(len(nums)-k):
            window_sum = window_sum + nums[i+k] - nums[i]
            maxval = max(maxval,window_sum)
        # print(maxval)
        return maxval/k