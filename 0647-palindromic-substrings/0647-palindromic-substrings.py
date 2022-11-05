class Solution:
    def countSubstrings(self, s: str) -> int:
        
        
        # 1. If string!=palindrome then output=len(s)
        # 2. ababa, gfhgfgjhjk

        
        c=0
  
        for i in range(len(s)):
            for j in range(len(s),-1,-1):
                if i==j:
                    break
                if s[i:j] == s[i:j][::-1]:
                    c+=1
        return c