class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        a_cost=0
        diffs=[]
        
        for i in costs:
            a_cost+=i[0]
        
        for j in range(len(costs)):
            diffs.append(costs[j][1]-costs[j][0])
        
        diffs.sort()
        minus=0
        for k in range(len(diffs)):
            minus+=diffs[k]
            if k==(len(costs)/2)-1:
                break
        
        total_cost = a_cost+minus
        return total_cost