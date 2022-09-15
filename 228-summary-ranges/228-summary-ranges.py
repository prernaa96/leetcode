class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        string=""
        start=-1
        end = 2**31-1
        count=0
        maxcount=-1
        ans=[]
        i=1
        
        for i in range(1,len(nums)):
            if nums[i-1]+1 == nums[i]:
                count+=1
                continue
            elif count>0:
                ans.append(f"{nums[i-count-1]}->{nums[i-1]}")
                # print("--",ans)
                count=0    
            else:
                ans.append(str(nums[i-1]))
            print(ans,count,i)   
            
        if count>0:
            # print("here")
            ans.append(f"{nums[i-count]}->{nums[i]}")
        if not count and len(nums) >1:
            ans.append(str(nums[i]))
        if len(nums) ==1:
            ans.append(str(nums[0]))   
          
        return ans
             
            
                
          
               
            
                