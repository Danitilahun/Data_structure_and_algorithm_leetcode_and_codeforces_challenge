class Solution:
    def rob(self, nums: List[int]) -> int:
        # Recursion Solution , Time complexity  -> O(2^n) , Space complexity  -> O(2^n) 
        # def helper(idx):
        #     if idx == 0: return nums[idx]
        #     if idx < 0 : return 0

        #     left = nums[idx] + helper(idx - 2)
        #     right = 0 + helper(idx -1)

        #     return max(left, right)
        # return helper(len(nums)-1)

        # DP Memoization 
        
        # dp = [-1] * len(nums)
        # def helper(idx):
        #     if idx == 0: return nums[idx]
        #     if idx < 0 : return 0

        #     if dp[idx] != -1: return dp[idx]

        #     left = nums[idx] + helper(idx - 2)
        #     right = 0 + helper(idx -1)

        #     dp[idx] = max(left, right)

        #     return dp[idx]

        # return helper(len(nums)-1)

        # DP tabulation 
        length = len(nums)
        dp = [-1] * length
        dp[0] = nums[0]
        answer = dp[0] 

        for idx in range(1,length):
            take = nums[idx] + (dp[idx-2] if idx - 2 >= 0 else 0)
            not_take = 0 + dp[idx-1]
            
            dp[idx] = max(take, not_take)
            
            answer = max(answer, dp[idx])
        return answer


