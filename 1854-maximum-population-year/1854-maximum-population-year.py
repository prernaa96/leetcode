class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        
        # 1950    1
        # 1960    2
        # 1961    1
        # 1970    2
        # 1971    1
        
        logs.sort()
        arr=[]
        x=[]
        y=[]
        maxval=0
        c=0
        min_year,max_year=0,0
        
        for i in range(len(logs)):
            arr.append([logs[i][0], True])
            arr.append([logs[i][1], False])
        
        arr.sort()
        
        for i,j in arr:
            if j==True:
                c+=1
                if c>maxval:
                    min_year=i
                
            else:
                c-=1
            maxval=max(c,maxval)

        return min_year
        
        
        
        
        
        
        
        
        