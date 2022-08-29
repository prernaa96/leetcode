class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        maxarea = 0
        i=0
        j=len(height)-1
        
        while i != j:
            minval = min(height[i],height[j])
            if maxarea < (minval * (j-i)):
                maxarea = minval * (j-i)
            if minval == height[i]:
                i+=1
            elif minval == height[j]:
                j-=1
#             else:
#                 print("here")
                
            
                
#             print(minval,maxarea)    
        
        return maxarea