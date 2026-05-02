class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        Summation = sum(nums)
        length = len(nums)
        F_prev = sum([i * nums[i] for i in range(length)])
        maximum = F_prev
        for index in range(1,length):
            F_index = F_prev + Summation - length* nums[length -index]
            maximum = max(maximum,F_index)
            F_prev = F_index
        
        return maximum