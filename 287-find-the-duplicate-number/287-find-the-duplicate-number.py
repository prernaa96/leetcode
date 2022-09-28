class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        nums.sort()
        
        ans=0
        # ans1=0
        for i in range(1,len(nums)):
            # print(nums[i])
            ans = nums[i-1] ^ nums[i]
            # print("ans-",ans)
            if ans ==0:
                return nums[i]
            
#         n=len(nums)  
#         for i in range(1,n): 
#             print("i=",i)
#             ans1 = ans1 ^ i
#         print("------",ans,ans1)
         
#         print(ans^ans1)
#         return abs(ans-ans1)
            
                