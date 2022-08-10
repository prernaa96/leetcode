class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        dic={}
        
        for i in range(len(s)):
            dic[s[i]] = dic.get(s[i],0) + 1
            
            # print(dic)
        
        for k,v in dic.items():
            if v == 1:
                ind = s.index(k)
                return ind
           
        return -1
            
                