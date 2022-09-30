class Solution:
    def myAtoi(self, s: str) -> int:

        s=s.strip()
        temp=""
        sign=0
        
        if len(s)==0:
            return 0
        
        start=1
        
        if s[0] =='+' or s[0]=='-' or s[0].isdigit():
            if s[0] =='+':
                sign=2
            elif s[0]=='-':
                sign=1
            else:
                start=0
        else:
            return 0
                
        for i in range(start, len(s)):
            if s[i].isdigit():
                temp=temp+s[i]
            else:
                break
        if sign==1:
            temp='-'+temp
        if temp=='-'or temp=='+' or len(temp)==0:
            return 0
        temp=int(temp)
      
        if temp>(2**31)-1:
            return 2147483647
        if temp< (-2**31):
            return -2147483648
            
        return temp
        
        