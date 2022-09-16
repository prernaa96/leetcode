class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dic={}
        
        if len(nums)==k:
            return nums
        
        for i in range(len(nums)):
            dic[nums[i]] = dic.get(nums[i],0)+1
        
        maxval=-10**4-1
        maxarr=[]
        
        for m,v in list(dic.items()):
            maxval=max(dic,key=dic.get)
            maxarr.append(maxval)
            del dic[maxval]
            if len(maxarr) == k:
                return maxarr
            
        