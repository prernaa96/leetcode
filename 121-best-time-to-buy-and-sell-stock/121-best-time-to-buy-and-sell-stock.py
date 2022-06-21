class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        total = 0
        minval = 0
        
        for i in range(1,len(prices)):
            total = max(total, prices[i] - prices[minval])
            if prices[i]<prices[minval]:
                minval = i
    
        return total
            