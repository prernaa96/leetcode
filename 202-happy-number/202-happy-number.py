class Solution:
    def isHappy(self, n: int) -> bool:
        
        if n ==1:
            return True
       
        checkset = set()
        def calc(n):
            total=0
            while n!=0:
                a = n% 10
                total = a*a + total
                n = n// 10
            return total    
       
        total = calc(n)
     
        if total == 1:
            return True
        
        while total != 1:
            total=calc(total)
           
            if total in checkset:
                return False
            else:
                if total ==1:
                    return True
                else:
                    checkset.add(total)  
          
    
    