class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        setnum = set(nums)
        if len(setnum)<3:
            return max(setnum)
        maxval = max(setnum)
        setnum.remove(maxval)
        maxval = max(setnum)
        setnum.remove(maxval)
        return max(setnum)
        print(setnum)
        