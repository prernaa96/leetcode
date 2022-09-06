class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        if len(s) == 1:
            return len(s)
        
        s=s.rstrip()
        ss=''
        for i in range(len(s)-1,-1,-1):
            # print("here",i)
            if s[i] == ' ':
                return len(ss)
            else:
                ss = ss + s[i]
                # print(ss)
                if i == 0:
                    return len(ss)
            