class Solution:
    def longestPalindrome(self, s: str) -> str:
        string=""
        strmax=-1
   
        for i in range(len(s)):
            # print("i--",i)
            l,r = i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                # print("w1",s[l],s[r])
                if strmax < r-l+1:
                    strmax = r-l+1
                    string = s[l:r+1]
                l-=1
                r+=1
            # print("flow check-----")   
            l,r = i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                # print("w2")
                if strmax < r-l+1:
                    strmax = r-l+1
                    string = s[l:r+1]
                l-=1
                r+=1  
            # print(string)   
        return string        
                        
                    
                        
                        
                                  