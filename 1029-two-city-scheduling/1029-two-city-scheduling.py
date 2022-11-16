class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        #Subtact a,b to get lower costs for a in length/2. Other half(<length/2)
        #will have lowest costs for b.
        #Sorted by a-b.
        

        diff = []
        for a, b in costs:
            diff.append([a-b, a, b])

        diff.sort()
        
        res = 0
        for i in range(len(diff)):
            if i<len(diff) / 2 :
                res += diff[i][1]
            else:
                res += diff[i][2]
            
        return res