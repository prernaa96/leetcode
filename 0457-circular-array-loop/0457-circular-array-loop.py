class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:

        n, visited = len(nums), set()
        for i in range(n):
            if i not in visited:
                local_s = set()
                while True:
                    if i in local_s: return True
                    if i in visited: break          
                    visited.add(i)
                    local_s.add(i)
                    prev, i = i, (i + nums[i]) % n
                    if prev == i or (nums[i] > 0) != (nums[prev] > 0): break
        return False
                    
                
        
        
        
        
        
        
        
        
        
        
        
#         slow=nums[0]
#         fast=nums[0]
        
#         while(1):
#             print("--->",slow,fast)
#             slow = nums[slow]
#             fast = nums[nums[fast]]
#             if slow==fast:
#                 print("in--",slow,fast)    
#                 break
                
#             print(slow,fast)       
            
#         slow== nums[0]
#         while(slow!=fast):
#             slow = nums[slow]
#             fast = nums[fast]
        
#         print("sl=",slow)
        
            
        