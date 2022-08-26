class Solution:
    def isValid(self, s: str) -> bool:
        
        opening = ["[", "{", "("]
        closing = ["]", "}", ")"]
        stack=[]
        
        for i in s:
            if i in opening:
                stack.append(i)
                # print(stack[-1])
            if i in closing:
                # print("in if 2",stack)
                
                if len(stack) == 0:
                    return False
                
                if stack[-1] == "[" and i == "]":
                    stack.pop()
                elif stack[-1] == "{" and i == "}":
                    stack.pop()
                elif stack[-1] == "(" and i == ")":
                    stack.pop() 
                else:
                    stack.append(i)
            
        if len(stack) == 0:
            return True
        else:
            return False
        
        
                   
                    
