class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        if a < 0 and b > 0 or a>0 and b<0:
            while b!=0 :
                andshift = (a&b) & 0xFFFFFFFF
                a= (a^b) & 0xFFFFFFFF
                b = (andshift <<1) 
            return a
        else:
            while b!=0 :
                andshift = (a&b) 
                a= (a^b) 
                b = (andshift <<1) 
            return a