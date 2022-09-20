class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        dic={}
        
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = i
            else:
                dic[nums[i]] = abs(i - dic[nums[i]])
                
                if (dic[nums[i]] <= k):
                    return True
        return False        
                
                