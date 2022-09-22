class Solution:
    def addDigits(self, num: int) -> int:
        
        while(num>9):
            add=0
            while(num):
                add=add+num%10
                num=num//10
            num=add
        return num
            
                
            
        # print(add)    
        
        
            
           