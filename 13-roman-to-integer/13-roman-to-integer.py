class Solution:
    def romanToInt(self, s: str) -> int:
        
        ch1={}
        ch2={}
        
        ch1={
            "IV":4,
            "IX":9,
            "XL":40,
            "XC":90,
            "CD":400,
            "CM":900
        }
        
        ch2 = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
        }      
            
        c=0
        i=0

        while i < len(s) :  
            # print(s[i],s[i+1])
            
            
            if i+1 < len(s) and (s[i]+s[i+1]) in ch1:
                c += ch1[s[i]+s[i+1]]
                i+=2
            elif s[i] in ch2:
                c += ch2[s[i]]
                i+=1
            else:
                i+=1
            print (c )   

            
            
        return c