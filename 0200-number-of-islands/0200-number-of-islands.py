class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        numOfIslands=0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                numOfIslands+=self.dfs(grid,i,j)
        
        return numOfIslands
    
    def dfs(self,grid,x,y):
        if x<0 or y<0 or x>=len(grid) or y>=len(grid[0]) or grid[x][y]=='0':
        
            return 0
        
        grid[x][y]='0'
  
    
        self.dfs(grid,x+1,y)

        self.dfs(grid,x-1,y)
    
        self.dfs(grid,x,y+1)
      
        self.dfs(grid,x,y-1)
        
        return 1
                    
                    
                    