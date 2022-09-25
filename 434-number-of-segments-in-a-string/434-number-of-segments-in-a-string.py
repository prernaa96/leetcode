class Solution:
    def countSegments(self, s: str) -> int:
        
        
        s = s.strip()
        if s == "":
            return 0
        c=0
        
        string = s.split(" ")
        for i in string:
            if i!="":
                c+=1
        return c
                