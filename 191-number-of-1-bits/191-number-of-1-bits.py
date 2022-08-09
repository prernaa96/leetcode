class Solution:
    def hammingWeight(self, n: int) -> int:
        
        c = bin(n).count('1')
        # print(n)
        return c