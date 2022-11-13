class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        ans = 0
        stack = []
        
        for i in range(n):
            l = len(stack)
            if l == 0 or height[i] < height[stack[-1]]:
                stack.append(i)
                
            else:
                while(l > 0 and height[stack[-1]] <= height[i]):
                    ht = height[stack.pop()]
                    l = l - 1
                    ans = ans + (0 if l == 0 else (min(height[i],height[stack[l - 1]]) - ht) * (i - stack[l - 1] - 1))                    
                stack.append(i)
        return ans
        
#         stack=[height[0]]
#         trap=0
#         minval=0
        
#         for i in range(1,len(height)):
#             if height[i]<height[i-1]:
#                 stack.append(height[i])
#             else:
#                 print("stack==",stack)
#                 while len(stack)>0 and height[i]>=stack[-1]:
#                     pops=stack.pop()
#                     minval=min(height[i],stack[-1]-pops)
#                     trap=trap+minval*(i-len(stack)-1)
#                     print("tr--",trap)
#                 stack.append(height[i])
           
#             print(stack,minval,trap)
                
            
        