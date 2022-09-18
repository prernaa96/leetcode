class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        xor = x^y
        ans=[]
        
        for i in bin(xor):
            ans.append(i)  
        tot = ans.count('1')
        return tot