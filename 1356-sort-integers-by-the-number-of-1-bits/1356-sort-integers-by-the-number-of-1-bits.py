class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        
        arr1=[]
        
        for i in arr:
            count=bin(i).count('1')
            arr1.append(count)
        
        arr_fin = [x for _,x in sorted(zip(arr1,arr))]
        return arr_fin