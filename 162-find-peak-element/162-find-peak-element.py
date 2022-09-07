class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        l = 0
        h = len(nums)-1
        
        while l < h:
            mid = (l+h)//2
            # print(mid,l,h)
            if nums[mid] < nums[mid+1]:
                l = mid+1
            else:
                h = mid
            # print(l,h)        
        return h    
           
        