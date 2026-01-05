class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        length = len(nums)
        for index in range(1,length):
            nums[index] += nums[index-1]
        
        return nums