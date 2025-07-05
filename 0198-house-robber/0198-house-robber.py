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

        # DP Memoization , Time complexity  -> O(n) , Space complexity  -> O(n)(Recursion Stack) + O(n)(DP memoization array)
        
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

        # DP tabulation , Time complexity  -> O(n) , Space complexity  -> O(n)(DP memoization array)

        # length = len(nums)
        # dp = [-1] * length
        # dp[0] = nums[0]
        # answer = dp[0] 

        # for idx in range(1,length):
        #     take = nums[idx] + (dp[idx-2] if idx - 2 >= 0 else 0)
        #     not_take = 0 + dp[idx-1]
            
        #     dp[idx] = max(take, not_take)
            
        #     answer = max(answer, dp[idx])
        # return answer

        # DP memory optimization , Time complexity  -> O(n) , Space complexity  -> O(1)

        length = len(nums)
        prev_value = nums[0]
        prev_prev_value = 0

        answer = prev_value

        for idx in range(1,length):
            take = nums[idx] + (prev_prev_value if idx - 2 >= 0 else 0)
            not_take = 0 + prev_value
            
            current_value = max(take, not_take)
            
            answer = max(answer, current_value)

            prev_prev_value = prev_value
            prev_value = current_value
            
        return answer


