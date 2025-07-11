class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        freq = [0]*(10002)
        dp = [-1]*(10002)
        for num in nums:
            freq[num]+=1
    
        def helper(idx):

            if idx <= 0 : return 0
            if dp[idx] != -1: return dp[idx]

            take = idx * freq[idx] + helper(idx - 2)
            not_take = 0 + helper(idx - 1)

            dp[idx] = max(take,not_take)

            return dp[idx]
        
        return helper(10001)
        