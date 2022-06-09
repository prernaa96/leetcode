class Solution:
    def mySqrt(self, x: int) -> int:
        
        copy = x
        
        if x == 0:
            return 0
        
        if x == 1:
            return 1
        
        while copy > 0:
            prev = copy
            copy = copy/2
            copy = int(copy)
            
            # print("cpp",copy)
            
            if copy*copy == x:
                return int(copy)
            
            if copy*copy <x:
                # print("in 1")
                for i in range(int(copy), int(prev)):
                    if i * i == x:
                        # print("in 2")
                        return i
                    else:
                        # print("in 3",i,copy)
                        if i*i <x and (i+1)*(i+1) >x:
                            # print("in 4")
                            return i
            
        