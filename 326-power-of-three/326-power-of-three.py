class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        if n == 0:
            return False
        
        if n ==1:
            return True
        
        for i in range(n):
            n = n/3
            print(n)
            
            if n % 3 != 0:
                if n != 1:
                    # print("in")
                    return False
            
            if n == 1:
                # print("true")
                return True
            