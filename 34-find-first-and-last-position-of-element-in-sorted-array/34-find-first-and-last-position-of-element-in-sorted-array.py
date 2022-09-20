class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if nums ==[]:
            return [-1,-1]
        
        l=0
        r=len(nums)-1
        ans=[]
        
        if l == r:
            if nums[l] == target:
                return [l,r]
            else:
                return [-1,-1]
        
        
        while (l<=r):
            mid = (l+r)//2
            if nums[mid] == target:
                l,r=mid,mid
                while l>=0 and nums[l]==target:
                    l=l-1
                while r<=len(nums)-1 and nums[r]==target:
                    r=r+1
                return [l+1,r-1]    
             
            if nums[mid] < target :
                # print("here")
                l=mid+1
            if nums[mid] > target :
                r=mid-1
        return [-1,-1]        