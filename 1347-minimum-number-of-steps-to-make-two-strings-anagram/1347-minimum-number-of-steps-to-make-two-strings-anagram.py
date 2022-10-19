class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        ans=0
            
        s_count=Counter(s)
        t_count=Counter(t)
        
        print(s_count,t_count)
        if(s_count==t_count):
            return 0
        
        for i in t_count:
            # print(t_count[i],s_count[i])
            if t_count[i]>s_count[i]:
                print("i if-",i)
                ans+=t_count[i]-s_count[i]
                print("ans if-",ans)
            elif i not in s_count:
                print("i elif-",i)
                ans+=1
                print("ans elif-",ans)
                
        return ans
        
        