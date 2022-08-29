class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if s ==" " or len(s)==1:
            return 1
        
        checked={}
        i=0
        length=0
        
        for j in range(len(s)):
            if s[j] in checked:
                # print(checked[s[j]] , i)
                if checked[s[j]] < i:
                    length=max(length, j-i+1)
                else:
                    i = checked[s[j]]+1
            else:
                length=max(length, j-i+1)
            checked[s[j]] = j
            # print(checked, length)
        return length    
                