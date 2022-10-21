class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        ans=[]
        i=0
        size=len(intervals)-1
        while i<size:
            if intervals[i][1]>=intervals[i+1][0] and intervals[i][0]<=intervals[i+1][1]:
                mini=min(intervals[i][0],intervals[i+1][0])
                maxi=max(intervals[i][1],intervals[i+1][1])
                intervals.pop(i)
                intervals.pop(i)
                intervals.insert(i,[mini,maxi])
                size-=1
            else:
                i+=1
        
        return intervals