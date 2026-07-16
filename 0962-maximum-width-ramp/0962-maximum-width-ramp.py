class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:

        monotonic_stack = [(nums[0],0)]
        n = len(nums)
        for ind in range(1,n):
            if monotonic_stack[-1][0] > nums[ind]:
                monotonic_stack.append((nums[ind], ind))
                
        maximum_ramp_width = 0
        for j in range(n-1,-1,-1):
            while monotonic_stack and nums[j] >= monotonic_stack[-1][0]:
    
                maximum_ramp_width = max(maximum_ramp_width, j - monotonic_stack[-1][1])
                monotonic_stack.pop()
            
        
        return maximum_ramp_width
        