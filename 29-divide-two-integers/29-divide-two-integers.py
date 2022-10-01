class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        flag1=False
        flag2=False
        if divisor<0:
            flag1=True
            divisor=-(divisor)
        if dividend<0:
            flag2=True
            dividend=-(dividend)
        c=0
        c2=1
        temp=divisor
        
        while(dividend>=divisor):
            temp=divisor
            c2=1
            while(dividend>=temp):
                c+=c2
                dividend=dividend-temp
                temp+=temp
                c2+=c2
        
        if flag1 and not flag2 or not flag1 and flag2:
            c=-(c)
        if flag1 and flag2:
            c=c
        if (c > 2 ** 31 - 1):
            c = 2 ** 31 - 1
        if (c < -2 ** 31):
            c = -2 ** 31
        return c
        
