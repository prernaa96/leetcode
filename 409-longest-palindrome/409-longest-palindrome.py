class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        dic={}
        flag=False
        for i in range(len(s)):
            dic[s[i]] = dic.get(s[i],0)+1

        c=0
        maxval=0
        for v in dic.values():
            if v%2 == 0:
                c=c+v
            else:
                c=c+v-1
                flag=True
        
        if flag==True:
            c=c+1
        
        return c
                