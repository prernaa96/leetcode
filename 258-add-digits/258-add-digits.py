class Solution:
    def addDigits(self, num: int) -> int:
        
        # add=0
        # while num:
        #     a = num % 10
        #     print(a)  
        #     num = num//10
        #     print("---",num)  
        #     add = add+a 
        #     print("add-",add)
        #     if num == 0:
        #         print(num)
        #         num=add
        # print(add)    
        
        if num ==0:
            return 0
        if num%9 ==0:
            return 9
        if num>9:
            return num%9
        if num<=9:
            return num
        
            
           