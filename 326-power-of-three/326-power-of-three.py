class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        if n == 0:
            return False
        
        if n ==1:
            return True
        
        for i in range(n):
            n = n/3
            
            if n % 3 != 0:
                if n != 1:
                    return False
            
            if n == 1:
                return True
            