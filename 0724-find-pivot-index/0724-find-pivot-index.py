class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        """
        Approach 1: Using nested loop
        - Loop over nums, for each index use two loop that somes sum to the left of the index and
        sum to the index's right.
        - Check that those sum and if they are equal return the index

        Time Complexity : O(N^2)
        Space Complexity : O(1)

        Approach 2: Using Prefix sum
        - Calculate total sum of nums, store the result in variale named total_sum
        - Initialize a variable left_sum to 0
        - Loop over nums and check if right_sum = total_sum - left_sum - nums[index]
        - If they are equal return that index

        Edge cases: 
        - When index is 0 -> Handled
        - When there is only one element -> Handled


        Time Complexity : O(N)
        Space Complexity : O(1)
        """

        total_sum = sum(nums)
        left_sum = 0
        length = len(nums)
        for index in range(length):
            right_sum = total_sum - left_sum - nums[index]
            if right_sum == left_sum:
                return index
            
            left_sum+=nums[index]
        
        return -1
