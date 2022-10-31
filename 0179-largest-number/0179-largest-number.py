class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        
        # 1. sort by first number
        # 2. If both 1st digits are same then sort by next two digits
        # 3. append to string
        
        def func(x,y):
            if x+y>y+x:
                return 1
            elif x==y:
                return 0
            else:
                return -1
        
        nums=[str(num) for num in nums]
        
        nums.sort(key=cmp_to_key(func),reverse=True)
        
        ans=""
        ans="".join(nums)
        if all(num == "0" for num in nums):
            return "0"
        return ans
        