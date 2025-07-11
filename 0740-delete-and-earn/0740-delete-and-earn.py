class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        freq = [0]*(10002)

        for num in nums:
            freq[num]+=1

        dp = [-1]*(10002)

        # DP - Memoization
    
        # def helper(idx):

        #     if idx <= 0 : return 0
        #     if dp[idx] != -1: return dp[idx]

        #     take = idx * freq[idx] + helper(idx - 2)
        #     not_take = 0 + helper(idx - 1)

        #     dp[idx] = max(take,not_take)

        #     return dp[idx]
        
        # return helper(10001)

        # DP - Tabulation

        dp[0] = 0
        dp[1] = freq[1]
        answer = dp[1]
        for idx in range(2,10002):

            take = idx * freq[idx] + dp[idx-2]
            not_take = 0 + dp[idx-1]

            dp[idx] = max(take, not_take)

            answer = max(answer,dp[idx])
        
        return answer
            
        