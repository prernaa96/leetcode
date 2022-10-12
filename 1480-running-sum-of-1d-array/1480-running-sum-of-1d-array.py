class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        run=0
        runarr=[]
        for i in nums:
            run+=i
            runarr.append(run)
        return runarr