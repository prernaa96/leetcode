class Solution:
    def climbStairs(self, n: int) -> int:
        
        one=1
        two=2
        
        if n == 1 or n == 2 or n == 3:
            return n
        
        else:
            for i in range(2,n):
                temp = one + two
                one = two
                two = temp
            return two
        