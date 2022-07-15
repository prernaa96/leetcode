class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        
        s1 = "".join(c for c in s if c.isalnum()).lower()
        # print(s1,s)
        
        if s1 == s1[::-1]:
            return True
        return False
        