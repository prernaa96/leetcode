class Solution:
    def decodeString(self, s: str) -> str:
        
        stack=[]
        for i in range(len(s)):
            if s[i]!="]":
                stack.append(s[i])
            else:
                string=""
                while stack[-1] != '[':
                    string=stack.pop()+string
                stack.pop()
                
                checkNum=""
                while(stack and stack[-1].isdigit()):
                    checkNum=stack.pop()+checkNum
                stack.append(int(checkNum) * string)
        ans=""
        for i in stack:
            ans+=i
        return ans