class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        dic1={}
        dic2={}
        
        for i in (t):
            dic2[i] = dic2.get(i,0)+1
        for j in s:
            dic1[j] = dic1.get(j,0)+1    
        
        res = {key: dic2[key] - dic1.get(key, 0)
                       for key in dic2.keys()}
        for i in res:
            if res[i]!=0:
                return i