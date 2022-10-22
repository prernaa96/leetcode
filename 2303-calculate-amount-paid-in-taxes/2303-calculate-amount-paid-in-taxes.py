class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        
        ans=0
        check=0
        flag=False
        
        diff=brackets[0][0]
        for i in range(len(brackets)):
            check+=diff
            if check>income:
                prev=check-diff
                diff=abs(income-prev)
                flag=True
            ans+=(diff* (brackets[i][1])/100)
            if i+1<len(brackets):
                diff = brackets[i+1][0]-brackets[i][0]
            if flag==True:
                break        
        return ans