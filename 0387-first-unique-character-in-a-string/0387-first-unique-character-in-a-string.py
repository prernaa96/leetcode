class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        dic={}
        key=""
        
        for i in range(len(s)):
            dic[s[i]] = dic.get(s[i],0)+1
        
        for k,v in dic.items():
            if v == 1:
                key=k
                break
        
        if key=="":
            return -1
        index=s.index(key)
        return index