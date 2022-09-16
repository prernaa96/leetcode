class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        # print(math.log2(n))
        if n<=0:
            return False
        
        if math.log2(n).is_integer():
            
            return True
        return False