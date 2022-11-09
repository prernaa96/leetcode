class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        pos=0
        arr=[]
        
        for i in range(1,n+1):
            arr.append(i)
        # print(arr)
        n=len(arr)
        
        j=0
        while(len(arr)>1):
            # print("********")
            val=j+k-1
            # print("v==",val)
            val=val%len(arr)
            pos = arr[val] % n
            # print(pos)
            del arr[val]
            j=val
            
            # print(arr)
            # print("----",val,j,pos)
        return arr[0]