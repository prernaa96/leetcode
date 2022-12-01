class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        
        # [4,2,3,4]
        # 2,4,4
        # 2,3,4
        # 2,3,4
        # 3,4,4
        
        nums.sort()
        c=0
        
        for i in range(1,len(nums)):
            l=0
            r=i-1
            while l<r:
                # print(nums[l],nums[r], nums[i])
                if nums[l]+nums[r] > nums[i]:
                    c+=(r-l)
                    r-=1
                else:
                    l+=1
        return c