class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        dic={}
        dic2={}
        
        for i in range(len(s)):
            dic[s[i]] = dic.get(s[i],0)+1
        
        for j in range(len(t)):
            dic2[t[j]] = dic2.get(t[j],0)+1
            
        if dic == dic2:
            return True
        else:
            return False
        
                
            