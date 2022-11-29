class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        #Path=[0] adds element 0 to path
        def dfs(start,graph,result,path=[0]):
            #check if node = n-1 and append existing calculated path
            if start==len(graph)-1:
                result.append(path)
            
            #DFS and keep track of the path created to reach last node
            for i in graph[start]:
                print(path)
                dfs(i, graph,result,path+[i])
        
        result=[]
        dfs(0,graph,result)
        return result 
    
    
            
        
        
        
        