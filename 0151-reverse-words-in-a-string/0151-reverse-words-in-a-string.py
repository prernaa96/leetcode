class Solution:
    def reverseWords(self, s: str) -> str:
        
        # 1. Run a reverse loop
        # 2. Put words one by one in string
        # 3. Use strip to remove white spaces
        
        string=""
        string1=""
        s=s.strip()
        # print("s=",s)
        
        for i in range(len(s)-1,-1,-1):
            string1=s[i] + string1
            # print("string1-",string1)
            if s[i] == " " or i==0:
                string=(string+" "+string1.strip()).strip()
                string1=" "
            # print("string-",string)
            
        return string.strip()