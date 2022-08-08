class Solution:
    def reverseBits(self, n: int) -> int:
        
        n = bin(n)
        n = str(n)
        n = n[2:]
        
        n = n[::-1]+ (32 - len(n))*'0'
        n = int(n, 2)
        
        return n
        