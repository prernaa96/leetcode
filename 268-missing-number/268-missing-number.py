class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        sum1=0
        sum2=0
        for i in range(len(nums)):
            sum1+=i+1
            sum2+=nums[i]
            
        # print(sum1-sum2)    
        return sum1-sum2