class Solution:
    def countPrimes(self, n: int) -> int:
        c=0
        arr = [False]*n
        
        if n == 0 or n== 1 or n ==2:
            return 0
        
        p=2
        while(p*p <= n):
            # print(p)
            if(arr[p]==False):
                for i in range(p*p, n, p):
                    # print(arr,i)
                    arr[i] = True
            p+=1
        for i in arr:
            if i == False:
                c+=1
        return c-2        
        
#         def prime(n):
#             for i in range(2,n//2):
#                 if n%i == 0:
#                     return False
#             return True    
        
#         for i in range(3,n,2):
#             print(i)
#             isprime = prime(i)
#             if isprime:
#                 total+=1
#         return total + 1   