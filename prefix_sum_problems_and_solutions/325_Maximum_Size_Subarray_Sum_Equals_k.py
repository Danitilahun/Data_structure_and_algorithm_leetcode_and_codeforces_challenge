# 325. Maximum Size Subarray Sum Equals k : https://leetcode.ca/2016-10-20-325-Maximum-Size-Subarray-Sum-Equals-k/

"""
Description
Given an integer array nums and an integer k, return the maximum length of a subarray that sums to k. If there is not one, return 0 instead.

Example 1:
	Input: nums = [1,-1,5,-2,3], k = 3
	Output: 4
	Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.

Example 2:
	Input: nums = [-2,-1,2,1], k = 1
	Output: 2
	Explanation: The subarray [-1, 2] sums to 1 and is the longest.

Constraints:
	1 <= nums.length <= 2 * 10^5
	-10^4 <= nums[i] <= 10^4
	-10^9 <= k <= 10^9

Link: https://leetcode.ca/2016-10-20-325-Maximum-Size-Subarray-Sum-Equals-k/
"""

from typing import List

def maxSubArrayLen(nums: List[int], k: int) -> int:
    
	n = len(nums)
	ans = 0
	prefix_map = {0: -1}
	sum_val = 0
 
	for i in range(n):
     
		sum_val += nums[i]
  
		if sum_val - k in prefix_map:
			ans = max(ans, i - prefix_map[sum_val - k])
		
		if sum_val not in prefix_map:
			prefix_map[sum_val] = i
   
	return ans
