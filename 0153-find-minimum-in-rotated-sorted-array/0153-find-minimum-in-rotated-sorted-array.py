class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # 4,5,6,7,8,0,1,2
        # 3,4,5,1,2
        # 11,13,15,17
        
        l=0
        r=len(nums)-1
        minval=nums[0]
        
        while(l<=r):
            
            if nums[l] < nums[r]:
                minval = min(minval, nums[l])
                return minval
            
            mid=(l+r)//2
            minval=min(minval,nums[mid])

            
            if nums[mid]>=nums[l]:
                l=mid+1      
            else:
                r=mid-1            
        return minval
