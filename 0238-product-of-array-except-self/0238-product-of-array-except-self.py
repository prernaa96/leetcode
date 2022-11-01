class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
   
        ans=[]
        prefix=[1]
        mult=1
        for i in nums:
            mult = mult*i
            prefix.append(mult)
        
        suffix=[1]
        mults=1
        for j in reversed(nums):
            mults = mults*j
            suffix.append(mults)
          
        suffix.pop()
        suffix.reverse()
      
        
        for i in range(len(nums)):
            ans.append( prefix[i]*suffix[i] )
        
        return ans
            
            
        
    
    
    
        return []
        