class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        stack=[]
        ans=""

        for i in s:
            if not stack:
                stack.append([i,1])
                continue
            if i ==stack[-1][0]:
                stack[-1][1]+=1
            else:
                stack.append([i,1])
            
            if stack[-1][1]==k:
                stack.pop()
        for i in range(len(stack)):
            ans=ans+(stack[-1][0]*stack[-1][1])
            stack.pop()
        return ans[::-1]
            