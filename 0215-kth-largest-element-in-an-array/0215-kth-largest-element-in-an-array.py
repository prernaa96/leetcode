class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heap=[]
        heapify(heap)
        
        #Add all elements to heap
        for i in nums:
            heappush(heap,i)
        # print(heap)
        
        #Find number of elements to pop
        ranges = len(nums)-k
        
        #Get first element of remaining elements which will be minimum of elements in list byt kth larget num
        for i in range(ranges):
            heappop(heap)
        # print(heap)
        
        return heap[0]