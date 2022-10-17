class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
#             0,1
        
#      1,0    1,1      1,2
    
#             2,1
        if image[sr][sc] == color :
            return image
        
        self.dfs(image,sr,sc,color,image[sr][sc])
        return image
   
    def dfs(self,image,sr,sc,color,image_curr):
        
        if sc<0 or sr<0 or sr>=len(image) or sc>=len(image[0]):
            return
        if image_curr!=image[sr][sc] :
            return
    
        image[sr][sc]=color
        self.dfs(image,sr-1,sc,color,image_curr)
        self.dfs(image,sr+1,sc,color,image_curr)
        self.dfs(image,sr,sc-1,color,image_curr)
        self.dfs(image,sr,sc+1,color,image_curr)
        
        
        
        
    