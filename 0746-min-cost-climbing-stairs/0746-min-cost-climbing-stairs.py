class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        n = len(cost)
        dp = [-1] *n

        def Climbing_Stairs(index):
            
            if index == n:
                return 0
            if dp[index] != -1: return dp[index]
            
            take_one_step = cost[index] + Climbing_Stairs(index + 1)
            take_two_step = float("inf")
            if index + 2 <= n:
                take_two_step = cost[index]  + Climbing_Stairs(index + 2)
            
            dp[index] = min(take_one_step, take_two_step)
            
            return dp[index]

        return min(Climbing_Stairs(0),Climbing_Stairs(1))