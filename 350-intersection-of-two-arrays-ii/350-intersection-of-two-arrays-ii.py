class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
      
        dic1={}
        dic2={}
        ans=[]
        
        for i in range(len(nums1)):
            dic1[nums1[i]] = dic1.get(nums1[i],0)+1  
        
        for j in range(len(nums2)):
            dic2[nums2[j]] = dic2.get(nums2[j],0)+1
        val=0
        for key in dic1.keys():
            if key in dic2.keys():
                if dic1[key] > dic2[key]:
                    val = dic2[key]
                elif dic1[key] < dic2[key]:
                    val = dic1[key]
                else:
                     val = dic1[key]
        
                for k in range(val):
                    ans.append(key)   
        return ans