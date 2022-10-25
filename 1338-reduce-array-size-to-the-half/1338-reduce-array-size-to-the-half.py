class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
        n=len(arr)/2
        c=0
        c1=0
        dic={}
        
        for i in arr:
            dic[i]=dic.get(i,0)+1
        
        for k in sorted(dic, key=dic.get, reverse=True):
            c+=dic[k]
            c1+=1
            if c>=n:
                return c1