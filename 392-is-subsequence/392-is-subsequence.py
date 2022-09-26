class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        chars=[]
        string=""
        
        i,j=0,0
        
        while(j!=len(t) and i!=len(s)):
            if s[i] == t[j]:
                string+=s[i]
                i+=1
                j+=1
            else:
                j+=1
        print(string)
        
        if string == s:
            return True
        return False
            
            
            
                
                