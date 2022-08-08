class Solution:
    def reverseBits(self, n: int) -> int:
        
        n = bin(n)
        n = str(n)
        n = n[2:]
        
        rev_str = n[::-1]+ (32 - len(n))*'0'
        rev_bin = int(rev_str, 2)
        
        return rev_bin
        