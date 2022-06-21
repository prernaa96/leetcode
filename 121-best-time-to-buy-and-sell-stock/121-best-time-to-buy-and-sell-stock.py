class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        total = 0
        minval = prices[0]
        
        for i in range(1,len(prices)):
            total = max(total, prices[i] - minval)
            if prices[i]<minval:
                minval = prices[i]
    
        return total
            