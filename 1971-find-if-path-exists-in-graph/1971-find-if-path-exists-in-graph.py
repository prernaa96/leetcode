class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph=self.createGraph(edges)
        return self.checkpath(graph,source,destination,set())
        
    def createGraph(self,edges):
        graph={}
        for i in (edges):
            one,two=i
            if one not in graph:
                graph[one]=[]
            if two not in graph:
                graph[two]=[]   
            graph[one].append(two)
            graph[two].append(one)
        return graph
        
    def checkpath(self,graph,src,dest,vis):
        print(src,dest)
        if src==dest:
            return True
        if src in vis:
            return False
        vis.add(src)
        for i in graph[src]:

            if self.checkpath(graph,i,dest,vis):
                return True
        return False
        
        
        
        
            
        
        

    
        
            