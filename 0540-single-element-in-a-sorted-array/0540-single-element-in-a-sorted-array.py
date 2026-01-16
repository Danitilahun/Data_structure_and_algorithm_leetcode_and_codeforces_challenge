class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """
        Approach 1: using XOR property 
        """

        unique = nums[0]
        length = len(nums)
        for index in range(1,length):
            unique ^= nums[index]
        
        return unique
