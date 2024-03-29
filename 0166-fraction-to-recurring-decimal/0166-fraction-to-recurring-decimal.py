from decimal import Decimal

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
      
        sign = '' if numerator * denominator >= 0 else '-'
        numerator, denominator = abs(numerator), abs(denominator)
        
        integer, remainder = divmod(numerator, denominator)
        
        decimal = ''
        seen = {}
        
        while remainder > 0:
            # last_remainder = remainder
            seen[remainder] = len(decimal)
            digi, remainder = divmod(remainder * 10, denominator)
            
            decimal += str(digi)

            if remainder in seen:
                index = seen[remainder]
                decimal = decimal[:index] + '(' + decimal[index:] + ')'
                break

        ans = sign + str(integer)
        if decimal:
            ans += '.' + decimal
        return ans


            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        # 1. Find remainder values
        # 2. Add to dict: {quotient:remainder}
        # 3. If same remainder
#         neg=False
#         if numerator==0:
#             return "0"
#         if denominator<0 and numerator>0:
#             neg=True
#             denominator=abs(denominator)
        
#         dic={}
#         ans=0
#         ans = Decimal(numerator)/Decimal(denominator)
        
#         ans1=str(ans)
        
#         if ("." not in ans1):
#             return ans1
        
#         int_str = ans1.split(".")[0]
#         deci_str = ans1.split(".")[1]
#         print("deci_str==",deci_str)
        
#         mod = int(Decimal(numerator)%Decimal(denominator))
#         quo=""
#         i=0
#         x=0
#         while(i<len(deci_str)):
#             quo = str(mod/denominator).split(".")[1][0]
#             if mod in dic:
#                 x=x+1
#             dic[mod] = {quo:x}
#             i+=1
#             mod = int(str(mod)+'0')%denominator

#         print(dic) 
#         ans=""
#         ans1=""
        
#         for i,j in dic.items():
#             for k in j:
#                 if j[k] ==0 and not ans1:
#                     print("in", k)
#                     ans=ans+str(k)
#                 else:
#                     ans1+=k
                    
#         if ans1:
#             ans+="("+ans1+")"
#         ans=int_str+"."+ans
#         if neg==True:
#             ans="-"+ans
#         return ans         
        
                
        
            
            
        
    
    
    
    
    