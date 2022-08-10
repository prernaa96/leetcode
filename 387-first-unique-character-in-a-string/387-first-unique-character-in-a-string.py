class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        a=0
        for i in range(len(s)):
            a=s.count(s[i])
            # print(a)
            if a == 1:
                return i
        return -1
            
                