class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp=[-1]*n
        def count_distinct_ways(step_sum):
            if step_sum > n:
                return 0
            if step_sum == n:
                return 1
            if dp[step_sum] != -1:
                return dp[step_sum]
            
            one_step_move = count_distinct_ways(step_sum+1)
            two_step_move = count_distinct_ways(step_sum+2)

            dp[step_sum] = one_step_move + two_step_move

            return dp[step_sum]
        
        return count_distinct_ways(0)