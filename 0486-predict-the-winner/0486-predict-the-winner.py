class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        def helper(left: int, right: int, turn: bool):
            
            if left >= right:
                return nums[left]
            
            take_from_left = (nums[left] if turn else -nums[left]) + helper(left+1,right, not turn)
            take_from_right = (nums[right] if turn else -nums[right]) + helper(left,right-1, not turn)

            return max(take_from_left, take_from_right) if turn else min(take_from_left, take_from_right)
        
        game = helper(0,len(nums)-1, True)

        return True if game >= 0 else False