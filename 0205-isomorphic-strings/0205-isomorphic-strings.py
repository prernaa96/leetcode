class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        dic={}
        
        if len(set(s))!=len(set(t)):
            return False
        
        for i in range(len(s)):
            if s[i] not in dic:
                 dic[s[i]] = t[i]
            else:
                if t[i] != dic[s[i]]:
                    return False
        return True
                    
        
        
        
        
            
            