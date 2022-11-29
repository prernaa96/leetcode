class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        stack = []
        ans=""
        
        for i in range(len(s)):
            # print(s[i],stack)
            if not stack:
                stack.append([s[i],1])
                continue
                
            if s[i] == stack[-1][0]:
                stack[-1][1]+=1
                # print(stack)
            else:
                stack.append([s[i],1])
            
            if stack[-1][1] == k:
                stack.pop()
            
            # print("===>",stack)
            
        for i in stack:
            ans = ans+i[0]*i[1]
        return ans
        
            