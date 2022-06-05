class Solution:
    def romanToInt(self, s: str) -> int:
        c=0
        i=0
        while i < len(s) :  
            
            if s[i] == 'L':
                c=c+50
            elif s[i] == 'V':
                c=c+5    
            elif s[i] == 'D':
                c=c+500
            elif s[i] == 'M':
                c=c+1000     
            
            elif s[i] == 'I':
                if i+1 < len(s) and s[i+1] == 'V':
                    i+=1
                    c=c+4
                elif i+1 < len(s) and s[i+1] == 'X':
                    i+=1
                    c=c+9
                else:    
                    c=c+1
            
            elif s[i] == 'X':
                if i+1 < len(s) and s[i+1] == 'L':
                    i+=1
                    c=c+40 
                elif i+1 < len(s) and s[i+1] == 'C':
                    i+=1
                    c=c+90
                else:    
                    c=c+10
                    
            elif s[i] == 'C':
                if i+1 < len(s) and s[i+1] == 'D':
                    i+=1
                    c=c+400       
                elif i+1 < len(s) and s[i+1] == 'M':
                    i+=1 
                    c=c+900
                else:
                    c=c+100
            
            i+=1      
        return c