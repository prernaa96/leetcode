class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        seq=[nums[0]]
        for i in nums:
            if i>seq[-1]:
                seq.append(i)
            elif i<seq[0]:
                seq[0]=i
            else:
                # print("------",i,seq)
                l=0
                r=len(seq)-1
                while(l<r):
                    mid=(l+r)//2
                    if i>seq[mid]:
                        l=mid+1
                    else:
                        r=mid
                seq[l]=i
        return len(seq)
                