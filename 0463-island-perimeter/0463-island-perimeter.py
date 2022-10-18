class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        tot=0
        vis=set()
        
        
        def dfs(grid,x,y):
            if(x,y) in vis: return 0

            if x<0 or y<0 or x>=len(grid) or y>=len(grid[0]) or grid[x][y]==0:
           
                return 1

            vis.add((x,y))
            return dfs(grid,x+1,y) + dfs(grid,x-1,y) + dfs(grid,x,y+1) + dfs(grid,x,y-1)
        
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(grid,i,j)
                        
        # return 0
    
    
        

        
        
        
        # 4-1+2+2+2+1+3-1