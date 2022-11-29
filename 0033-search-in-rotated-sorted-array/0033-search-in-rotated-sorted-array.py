class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
#         [4,5,6,7,0,1,2]
        
#         [1,2,4,5,6,7,0]
        
#         [7,0,1,2,4,5,6]

#         [4,5,6,7,0,1,2]

        l=0
        r = len(nums)-1
        
        while (l<=r):
            mid = (l+r)//2
            
            if nums[mid]==target:
                return mid
            
            elif nums[mid]>=nums[l]:
                if target < nums[mid] and target >=nums[l]:
                    r=mid-1
                else:
                    l=mid+1

            else:
                if target > nums[mid] and target <=nums[r]:
                    l=mid+1
                else:
                    r=mid-1
            
        return -1