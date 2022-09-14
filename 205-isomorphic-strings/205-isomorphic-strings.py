class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        dic={}
        
        for i in range(len(s)):
            if s[i] not in dic :
                dic[s[i]] = t[i]
            else:
                print(i,dic[s[i]], t[i])
                if dic[s[i]] != t[i]:
                    print(dic) 
                    return False
        if len(set(dic.values())) != len(dic.values()): 
            return False           
              
                    
        return True