class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        v=[]
        
        for i in nums:
            if i not in v:
                v.append(i)
                if nums.count(i) > len(nums)//2:
                    return i
        
        