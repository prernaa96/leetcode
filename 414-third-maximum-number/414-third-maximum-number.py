class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        setnum = set(nums)
        if len(setnum)<3:
            return max(setnum)
        sort = sorted(setnum)
        return sort[len(sort)-3]
        # print(setnum)
        