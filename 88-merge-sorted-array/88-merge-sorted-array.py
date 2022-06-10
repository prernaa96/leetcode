class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        c=0
        nums1.extend(nums2)
        nums1.sort()
        for i in range(m+n):
            if 0 in nums1 and n!=0:
                nums1.remove(0)
                c+=1
            if c == n:
                break
        