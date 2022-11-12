class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        flag=False
        min_len=len(nums)
        
        #Prefix sum
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        nums = [0]+nums
        # print(nums)
        
        i=1
        for j in range(1,len(nums)):
            while nums[j]-nums[i-1]>=target:
                flag=True
                min_len=min(j-i+1, min_len)
                i+=1
                
        if flag==True:
            return min_len
        else:
            return 0
        