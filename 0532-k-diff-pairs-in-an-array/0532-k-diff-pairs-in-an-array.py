class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        ans=set()
        dic={}
        c=0
        
        for i in range(len(nums)):
            if nums[i]-k <0:
                val = nums[i]-(-k)
            else:
                val = nums[i]-k
            dic[nums[i]] = val

            
        for k,v in dic.items():
            if v in nums:
                if (v,k) not in ans:
                    
                    if k==v and nums.count(v)<2:
                        continue
                        
                    ans.add((k,v))
        return len(ans)
        