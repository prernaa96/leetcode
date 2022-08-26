class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        ans=[]
        
        ans.append([1])
        if numRows == 1:
            return ans
        ans.append([1,1])
        if numRows == 2:
            return ans
        else:
            for j in range(numRows-2):
                val = ans[len(ans)-1]
                new=[]
                new.append(1)
                for i in range(1,len(val)):
                    tot = val[i]+val[i-1]
                    new.append(tot)
                new.append(1)
                ans.append(new)
                # print(ans)
                new=[]
                
        return ans    
            
            