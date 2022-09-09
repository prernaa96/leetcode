class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        
        def dfs(val):
            visited[val]=True
            for i in adj[val]:
                if visited[i]==False:
                    dfs(i)
            stack.append(val) 
            # print(stack)  
            
        def cycle():     
            ind =0
            
            while(len(stack)!=0):
                pos[stack[-1]] = ind
                ind+=1
                stack.pop()
           
            for i in range(numCourses):
                for j in adj[i]:
                    f = 0 if i not in pos else pos[i]
                    s = 0 if j not in pos else pos[j]
                    # print("------")  
                    # print(f,s)
                    if f >= s:
                        ans = False
                        return ans
            #     print("out")
            # print("hmm")    
            ans = True 
            return ans
            
        
        visited = [False]*numCourses
        adj = [[] for a in range(numCourses)]
        stack=[]
        pos=dict()
        ans=False
        
        for i in range(len(prerequisites)):
            adj[prerequisites[i][0]].append(prerequisites[i][1])
        # print(adj)  
        
        for i in range(numCourses):
            if visited[i] == False:
                dfs(i)
        
        ans=cycle()
        if ans ==True:
            return True
        else:
            return False
           
            