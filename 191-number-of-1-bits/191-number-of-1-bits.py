class Solution:
    def hammingWeight(self, n: int) -> int:
        
        c=0
        
        for i in range(32):
            if n&1:
                c+=1
            n = n >> 1    
        # print(c) 
        return c 