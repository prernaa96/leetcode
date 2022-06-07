class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=""
        lens = [len(i) for i in strs]
        minLen = min(lens)
        print(minLen)
        
        if len(strs) == 1:
            ans = strs[0]
        
        for i in range(minLen):
            flag=0
            for j in range(1,len(strs)):
                print(strs[j-1][i], strs[j][i])
                if strs[j-1][i] == strs[j][i]:
                    if flag == 0:
                        ans = ans + strs[j][i]
                        flag=1    
                else:
                    print("else=0--==",ans,flag)
                    if flag == 1:
                        ans = ans[:-1]
                        break 
                    print("ans else=",ans)     
                    return ans
                    
                    
        print("ans=",ans)  
        
        return ans
            
        
        