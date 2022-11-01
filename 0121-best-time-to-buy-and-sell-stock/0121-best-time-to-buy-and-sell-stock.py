class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #KADANE
        # max_end_here=max_end_here-prices[i]
        # print("--->",max_end_here)
        # if max_so_far < max_end_here:
        #     max_so_far = max_end_here
        # if max_end_here<0:
        #     max_end_here=0
        
        
        
        
        max_end_here = prices[0]
        max_so_far=0
        val=0
        
        for i in range(1,len(prices)):
            val = prices[i]-max_end_here
            # print(val)
            if max_so_far < val:
                max_so_far = val
            if prices[i]<max_end_here:
                max_end_here = prices[i]
            
        return max_so_far