class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        sums=0
        min_wind_size=10**9+1
        i=0

        for j in range(len(nums)):
            sums=sums+nums[j]
            while sums>=target:
                min_wind_size = min(min_wind_size, j-i+1)
                sums=sums-nums[i]
                i+=1
        
        if min_wind_size==10**9+1:
            return 0
                
        return min_wind_size
        
        
        
        
        
        
#         flag=False
#         min_len=len(nums)
        
#         #Prefix sum
#         for i in range(1,len(nums)):
#             nums[i]+=nums[i-1]
#         nums = [0]+nums
#         # print(nums)
        
#         i=1
#         for j in range(1,len(nums)):
#             while nums[j]-nums[i-1]>=target:
#                 flag=True
#                 min_len=min(j-i+1, min_len)
#                 i+=1
                
#         if flag==True:
#             return min_len
#         else:
#             return 0
        