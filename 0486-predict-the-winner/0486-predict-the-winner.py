class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n= len(nums)
        dp = [[-1 for _ in range(n)] for _ in range(n)]
        
        def helper(left: int, right: int, turn: int):
            
            if left == right:
                return nums[left]
            if dp[left][right] != -1: return dp[left][right]
            
            take_from_left = nums[left]*turn + helper(left+1,right, -turn)
            take_from_right = nums[right]*turn + helper(left,right-1, -turn)

            dp[left][right] = max(take_from_left, take_from_right) if turn==1 else min(take_from_left, take_from_right)
            return dp[left][right]

        return helper(0,len(nums)-1, 1) >= 0