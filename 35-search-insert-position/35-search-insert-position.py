class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        l=0
        r = len(nums)-1
        
        if target < nums[0]:
            return 0
        if target > nums[len(nums)-1]:
            return len(nums)
        
        while(l<r):
            mid = (l+r)//2
            # print(mid,l,r)
            if nums[mid] < target:
                l = mid+1
                # print("----",mid)
            elif nums[mid] > target:
                r = mid
                # print("-",mid)
            else:
                # print("here")
                return mid
        
        # print("++++",mid, l,r)
        return r
            