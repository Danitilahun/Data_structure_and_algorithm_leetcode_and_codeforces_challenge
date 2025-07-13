class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        def helper(left: int, right: int, turn: int):
            
            if left == right:
                return nums[left]
            
            take_from_left = nums[left]*turn + helper(left+1,right, -turn)
            take_from_right = nums[right]*turn + helper(left,right-1, -turn)

            return max(take_from_left, take_from_right) if turn==1 else min(take_from_left, take_from_right)
        
        game = helper(0,len(nums)-1, 1)

        return True if game >= 0 else False