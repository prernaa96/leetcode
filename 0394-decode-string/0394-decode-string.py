class Solution:
    def decodeString(self, s: str) -> str:
        
        stack=[]
        string=""
        
        for i in range(len(s)):
            if s[i] == "]":
                val=""
                while stack[-1]!="[":
                    val=stack.pop()+val
                stack.pop()
                nums=""
                while stack and stack[-1].isdigit():
                    nums=stack.pop()+nums 
                stack.append(int(nums)*val)
            else:
                stack.append(s[i])
        
        string="".join(stack)
        return string
        