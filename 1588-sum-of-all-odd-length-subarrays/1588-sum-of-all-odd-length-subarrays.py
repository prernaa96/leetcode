class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        
        total_sum=0
        initial_sum=sum(arr)
        total_sum+=initial_sum
       
        if len(arr)<3:
            return total_sum
        
        length=3
        
        while(length<len(arr)):
            
            curr=0
            
            for i in range(length):
                curr=curr+arr[i]
            total_sum+=curr
            
            for i in range(length,len(arr)):
                curr=curr+arr[i]-arr[i-length]
                total_sum+=curr
            length+=2
            
        if len(arr)%2!=0:
            total_sum+=sum(arr)
        return total_sum
            
           
        
        
        
        
            
            
                
    
           