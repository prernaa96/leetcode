class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        def dfs(src,graph,res,path=[0]):
            if src==len(graph)-1:
                res.append(path)

            for i in graph[src]:
                dfs(i,graph,res,path+[i])
        
        result=[]
        dfs(0,graph,result)
        return result 
    
    
            
        
        
        
        