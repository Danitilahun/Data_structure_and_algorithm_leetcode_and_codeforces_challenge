"""
Problem: 1590. Make Sum Divisible by P
Link: https://leetcode.com/problems/make-sum-divisible-by-p/

Given an array of positive integers nums, remove the smallest subarray (possibly empty) 
such that the sum of the remaining elements is divisible by p. It is not allowed to 
remove the whole array.

Return the length of the smallest subarray that you need to remove, or -1 if it's 
impossible.

Example 1:
Input: nums = [3,1,4,2], p = 6
Output: 1
Explanation: The sum of the elements in nums is 10, which is not divisible by 6. 
We can remove the subarray [4], and the sum of the remaining elements is 6, which 
is divisible by 6.

Example 2:
Input: nums = [6,3,5,2], p = 9
Output: 2
Explanation: We cannot remove a single element to get a sum divisible by 9. The 
best way is to remove the subarray [5,2], leaving us with [6,3] with sum 9.

Example 3:
Input: nums = [1,2,3], p = 3
Output: 0
Explanation: Here the sum is 6, which is already divisible by 3. Thus, we do not 
need to remove anything.

Constraints:
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
1 <= p <= 10^9
"""

class Solution:
    def minSubarray(self, nums: list[int], p: int) -> int:
        def mod(a: int, b: int) -> int:
            return (a % b + b) % b

        total_sum = sum(nums)
        
        if total_sum < p:
            return -1

        total = total_sum % p
        
        if total == 0:
            return 0

        n = len(nums)
        prefix_sum = 0
        ans = n
        index_map = {0: -1}

        for j, num in enumerate(nums):
            prefix_sum = mod(prefix_sum + num, p)
            index_map[prefix_sum] = j
            
            ai_p = mod(prefix_sum - total, p)
            
            if ai_p in index_map:
                ans = min(ans, j - index_map[ai_p])

        return ans if ans < n else -1
