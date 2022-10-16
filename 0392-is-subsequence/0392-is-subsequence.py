class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        i=0
        j=0
        
        while(i!=len(s) and j!=len(t)):
            # print("*******",i,j)
            if s[i]==t[j]:
                i+=1
                j+=1
            else:
                j+=1
        if i!=len(s) and j==len(t):
            return False
        return True
            
            
            
            
                
                