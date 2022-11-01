class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
#         [7,2,-2,-6]
#         [3,4,2]
        
#         1. create new arr of values = target-nums[i]
#         2. if nums[i]==value[j] where i!=j
#         3. Return indices
        
        values=[0]*len(nums)
        
        for i in range(len(nums)):
            values[i]=target-nums[i]
        
        for i in range(len(values)):
            if values[i] in nums:
                if i != nums.index(values[i]):
                    return [i,nums.index(values[i])]
            