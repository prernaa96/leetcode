class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heap=[]
        heapify(heap)
        
        for i in nums:
            heappush(heap,i)
        print(heap)
        
        ranges = len(nums)-k
        
        for i in range(ranges):
            heappop(heap)
        print(heap)
        
        return heap[0]