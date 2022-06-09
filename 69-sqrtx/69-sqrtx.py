class Solution:
    def mySqrt(self, x: int) -> int:
        
        copy = x
        
        if x == 0 or x == 1:
            return x
        
        while copy > 0:
            prev = copy
            copy = int(copy/2)
            
            if copy*copy == x:
                return int(copy)
            
            if copy*copy <x:
                for i in range(int(copy), int(prev)):
                    if i * i == x:
                        return i
                    else:
                        if i*i <x and (i+1)*(i+1) >x:
                            return i
            
        