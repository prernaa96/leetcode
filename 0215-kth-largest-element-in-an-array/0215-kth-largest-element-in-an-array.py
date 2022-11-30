class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        #opt2- https://leetcode.com/problems/kth-largest-element-in-an-array/discuss/1019513/Python-QuickSelect-average-O(n)-explained
        
        print(nums,k)
        if not nums: return
        pivot = random.choice(nums)
        left =  [x for x in nums if x > pivot]
        mid  =  [x for x in nums if x == pivot]
        right = [x for x in nums if x < pivot]
        
        print(pivot,left,mid,right)
        
        L, M = len(left), len(mid)
        #if k. is larger it will be in right probably
        if k <= L:
            return self.findKthLargest(left, k)
        elif k > L + M:
            print("-----",k-L-M)
            return self.findKthLargest(right, k - L - M)
        else:
            return mid[0]
        
        
#         heap=[]
#         heapify(heap)
        
#         #Add all elements to heap
#         for i in nums:
#             heappush(heap,i)
#         # print(heap)
        
#         #Find number of elements to pop
#         ranges = len(nums)-k
        
#         #Get first element of remaining elements which will be minimum of elements in list byt kth larget num
#         for i in range(ranges):
#             heappop(heap)
#         # print(heap)
        
#         return heap[0]