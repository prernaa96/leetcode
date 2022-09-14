class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        max_len = 0
        num_set = set(nums)
        for i in nums:
            if i - 1 not in num_set:
                num = i
                curr = 1
                while num + 1 in num_set:
                    num += 1
                    curr += 1
                max_len = max(max_len, curr)
        return max_len
#         length=0
#         maxlen=0
#         i=0
#         visited=set()
#         numsset = set(nums)
        
#         if len(nums)==0:
#             return 0
#         if len(nums)==1:
#             return 1
        
#         for i in range(len(nums)):
#             if nums[i]-1 not in numsset:
#                 length=1
#                 start=nums[i]
#                 visited.add(start)
#                 while start+1 in numsset:
#                     length+=1
#                     start+=1
#                     visited.add(start)   
#                 maxlen = max(maxlen,length) 
#         return maxlen        
                      
                
               