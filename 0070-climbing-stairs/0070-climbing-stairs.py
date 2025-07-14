class Solution:
    def climbStairs(self, n: int) -> int:

        if (n<=3):
            return n
        
        # dp=[-1]*n

        # def count_distinct_ways(step_sum):
        #     if step_sum > n:
        #         return 0
        #     if step_sum == n:
        #         return 1
        #     if dp[step_sum] != -1:
        #         return dp[step_sum]
            
        #     one_step_move = count_distinct_ways(step_sum+1)
        #     two_step_move = count_distinct_ways(step_sum+2)

        #     dp[step_sum] = one_step_move + two_step_move

        #     return dp[step_sum]
        
        # return count_distinct_ways(0)

        # dp=[-1]*n

        # dp[0] = 1
        # dp[1] = 2

        # for idx in range(2,n):

        #     dp[idx] = dp[idx-1] + dp[idx-2]
        
        # return dp[n-1]

        previous_previous = 1
        previous = 2

        for idx in range(2,n):

            current = previous + previous_previous
            previous_previous = previous
            previous = current
        
        return previous
            
