class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        ans=[]
        currind= 0
        
        for i in range(len(nums)):
            newTarget = target - nums[i]
            if newTarget in nums and i!= nums.index(newTarget):
                print(i,newTarget)
                ans.append(i)
                index = nums.index(newTarget)
                ans.append(index)
                break 
        return ans    