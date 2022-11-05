class Solution:
    def countSubstrings(self, s: str) -> int:
        
        
        # 1. If string!=palindrome then output=len(s)
        # 2. ababa, gfhgfgjhjk
        
        # if s != s[::-1]:
        #     return len(s)
        
        c=0
        count=0
        
        # if s==s[::-1]:
        for i in range(len(s)):
            for j in range(len(s),-1,-1):
                # print(i,j, s[i:j], s[i:j][::-1])
                if i==j:
                    break
                if s[i:j] == s[i:j][::-1]:
                    # print( s[i:j], s[i:j][::-1])
                    c+=1
                
             
                # print("c==",c)

        return c