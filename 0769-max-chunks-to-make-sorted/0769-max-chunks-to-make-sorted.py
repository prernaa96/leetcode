class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        
        if len(arr)==1:
            return 1
        
        if arr==sorted(arr):
            return len(arr)
        
        maxval=0
        ans=0
        for i in range(len(arr)):
            if arr[i]>maxval:
                maxval=arr[i]
            if i==maxval:
                ans+=1
        return ans
        