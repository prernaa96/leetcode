class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[0]*len(nums)
        
        prefix=[1]
        prod=1
        for n in nums:
            prod*=n
            prefix.append(prod) 
        
        suffix=[1]
        prod=1
        for n in reversed(nums):
            prod*=n
            suffix.append(prod)
        suffix.pop()
        suffix.reverse() 
        
        for i in range(len(nums)):
            ans[i] = prefix[i]*suffix[i]
        return ans    