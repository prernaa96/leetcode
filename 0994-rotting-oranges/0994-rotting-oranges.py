from collections import deque as queue
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
       
        q=queue()
        dRow = [ -1, 0, 1, 0]
        dCol = [ 0, 1, 0, -1]
        fresh=0
        minutes=0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    q.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1
        
        while q and fresh>0:
            for _ in range(len(q)):
                pops=q.popleft()
                x=pops[0]
                y=pops[1]

                for i in range(len(dRow)):
                    adjx = x+dRow[i]
                    adjy = y+dCol[i]
                    if (adjx >= 0 and adjy >= 0 and adjx < len(grid) and adjy <                                 len(grid[0]) and grid[adjx][adjy] == 1):
                        fresh-=1
                        grid[adjx][adjy]=2
                        q.append((adjx,adjy))
            minutes+=1
        if fresh==0:
            return minutes
        else: return -1
        
                    
                   
                    
        
        
                