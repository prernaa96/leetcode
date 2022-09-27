class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        c=0

        a = n/5
        b = a//5
        n=a+b
        print(n)

        while b>=5:
            b=b//5
            c=c+b
            print(b,c)
        n=n+c
            
        return int(n)
        
        
#         c=0
#         string=""
#         res = 1
     
#         for i in range(2, n+1):
#             res *= i
#         a=str(res)
#         if '0' not in a:
#             return 0
#         b=a[::-1]
#         for i in range(len(b)):
#             if b[i]!='0':
#                 string = b[:i]
#                 break
#         return len(string)