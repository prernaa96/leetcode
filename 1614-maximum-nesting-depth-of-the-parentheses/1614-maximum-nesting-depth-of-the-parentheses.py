class Solution:
    def maxDepth(self, s: str) -> int:
        
        stack=[]
        c=0
        maxval=0
        
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(s[i])
            if s[i] == ")":
                maxval=max(maxval, len(stack))  
                stack.pop()
        return maxval
        