class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        # i=1
        # j=nums[len(nums)]
        # prefix=0
        # suffix=0
        # print("-->",nums[j],suffix)
        left=0
        
        count=sum(nums)
        
        for j in range(len(nums)):
            right_sum = count-nums[j]-left
            if left == right_sum:
                return j
            left+=nums[j]
        return -1

            