class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        prefixSum = {0:-1}
        sums=0
        for i in range(len(nums)):
            sums+=nums[i]
            res=sums%k
            if res in prefixSum:
                if i-prefixSum[res]>1:
                    return True
            else:
                prefixSum[res]=i
        
        return False
    
        
   
  # 2,2,4,1,1      

        
        
        
        
        