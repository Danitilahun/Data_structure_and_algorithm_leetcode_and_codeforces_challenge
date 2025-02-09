"""
974. Subarray Sums Divisible by K

Problem Link: https://leetcode.com/problems/subarray-sums-divisible-by-k/description/

Given an integer array nums and an integer k, return the number of non-empty subarrays 
that have a sum divisible by k.

A subarray is a contiguous part of an array.

Example 1:
    Input: nums = [4, 5, 0, -2, -3, 1], k = 5
    Output: 7
    Explanation: There are 7 subarrays with a sum divisible by k = 5:
                 [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

Example 2:
    Input: nums = [5], k = 9
    Output: 0

Constraints:
    1 <= nums.length <= 3 * 10^4
    -10^4 <= nums[i] <= 10^4
    2 <= k <= 10^4
"""

from typing import List

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
       
        remainder_freq = {0: 1}
        prefix_sum = 0
        subarray_count = 0

        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k
            
            subarray_count += remainder_freq.get(remainder, 0)
            remainder_freq[remainder] = remainder_freq.get(remainder, 0) + 1
        
        return subarray_count


if __name__ == "__main__":
    solution = Solution()

    nums1 = [4, 5, 0, -2, -3, 1]
    k1 = 5
    result1 = solution.subarraysDivByK(nums1, k1)
    print(f"Test Case 1: {result1} (Expected: 7)")

    nums2 = [5]
    k2 = 9
    result2 = solution.subarraysDivByK(nums2, k2)
    print(f"Test Case 2: {result2} (Expected: 0)")
