class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        next1 = cost[len(cost) - 1]
        next2 = 0

        for i in range(len(cost) - 2, -1, -1):

            curr = cost[i] + min(next1, next2)
            next2 = next1
            next1 = curr
        
        return min(next1, next2)
        
        

