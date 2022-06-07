class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=""
        lens = [len(i) for i in strs]
        minLen = min(lens)
        
        if len(strs) == 1:
            ans = strs[0]
        
        for i in range(minLen):
            flag=0
            for j in range(1,len(strs)):
                if strs[j-1][i] == strs[j][i]:
                    if flag == 0:
                        ans = ans + strs[j][i]
                        flag=1    
                else:
                    if flag == 1:
                        ans = ans[:-1]
                        break    
                    return ans

        return ans
            
        
        