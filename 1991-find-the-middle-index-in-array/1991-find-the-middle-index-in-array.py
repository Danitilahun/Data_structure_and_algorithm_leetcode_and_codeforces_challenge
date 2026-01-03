class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        length = len(nums)
        for index in range(length):
            right_sum = total_sum - left_sum - nums[index]
            if right_sum == left_sum:
                return index
            
            left_sum+=nums[index]
        
        return -1