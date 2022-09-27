class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        ans=[]
        index=0
        maxval=-1
        
        for i in range(len(nums2)):
            if nums1[i] in nums2 :
                index = nums2.index(nums1[i])
                j=index+1
                
                while j <= len(nums2)-1:
                    if nums2[j]>nums2[index]:
                        ans.append(nums2[j])
                        j=0
                        break
                    else:
                        if j == len(nums2)-1:
                            ans.append(-1)
                        j+=1
                if index == len(nums2)-1:
                    ans.append(-1)
            if i == len(nums1)-1:
                return ans
                
                