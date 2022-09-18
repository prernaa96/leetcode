class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        if not a :
            return b
        if not b:
            return a
         
        while b!=0 :
            andshift = (a&b) & 0xffffffff
            a= (a^b) & 0xffffffff
            b = (andshift <<1) 
            
        if (a>>31)&1:
            return ~(a^0xffffffff)
            
        return a