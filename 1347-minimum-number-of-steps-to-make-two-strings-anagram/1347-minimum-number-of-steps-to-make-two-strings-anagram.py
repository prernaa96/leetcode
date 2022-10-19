class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        ans=0
            
        s_count=Counter(s)
        t_count=Counter(t)
        
        if(s_count==t_count):
            return 0
        
        for i in t_count:
            if t_count[i]>s_count[i]:
                ans+=t_count[i]-s_count[i]
            elif i not in s_count:
                ans+=1
                
        return ans
        
        