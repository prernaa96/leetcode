class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        if len(nums) == 1:
            return False
        
        dic={}
        for i in range (len(nums)):
            dic[nums[i]] = dic.get(nums[i],0)+1
        
        for k,v in dic.items():
            if dic[k] > 1:
                return True
        return False    
            