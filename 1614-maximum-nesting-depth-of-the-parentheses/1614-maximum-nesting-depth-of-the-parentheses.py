class Solution:
    def maxDepth(self, s: str) -> int:
        
        # if len(s)==0:
            
        
        stack=[]
        maxval=0
        
        for i in s:
            if i == '(':
                stack.append(i)
                maxval=max(maxval,len(stack))
            if i == ')':
                stack.pop()
                
        return maxval