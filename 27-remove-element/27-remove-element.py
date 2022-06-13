class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        c=0
        i=0
        
        if val not in nums:
            return len(nums)
        
        if len(nums) == 1:
            return 0
        
        while i < len(nums)-1:
            if nums[i] == val:
                if nums[i] == nums[len(nums)-1-c]:
                    c+=1
                else:
                    nums[i], nums[len(nums)-1-c] = nums[len(nums)-1-c], nums[i] 
                    print("after swap-", nums)
                    print("c=",c)
                    print("i=",i)
                    i+=1
            else:
                print("here", i)
                i+=1
                
            count = nums.count(val)
            diff = len(nums) - count

            if diff == 0:
                return 0

            if  i == diff:
                print("break", i+1, diff)
                return diff
                break
                   
                
        print(nums)        
        
        
        
        
        
        
        
        
        
        
#         for i in range(len(nums)):
#             if nums[i] == val:
#                 # if nums[i] == nums[len(nums)-1-c]:
#                 c+=1
#             else:
#                 print("in else")
#                 nums[i], nums[i-c] = nums[i-c], nums[i]
#             print(nums,i)        
            
#             count = nums.count(val)
#             diff = len(nums) - count
            
#             if diff == 0:
#                 return 0
            
#             if i+1 == diff:
#                 return diff
#                 break
                
             
             
        
        
        
        
        
        
        
        
        # for i in range(len(nums)-1):
        #     if nums[i] == val:
        #         if nums[i] != nums[len(nums)-1-c]:
        #             print(nums[len(nums)-1-c],c)
        #             nums[i], nums[len(nums)-1-c] = nums[len(nums)-1-c], nums[i]
        #             c+=1
        #         # else:
        #         #     nums[i], nums[len(nums)-1-c] = nums[len(nums)-1-c], nums[i]
        # print(nums)        