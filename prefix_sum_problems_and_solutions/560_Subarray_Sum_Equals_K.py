# 560. Subarray Sum Equals K: https://leetcode.com/problems/subarray-sum-equals-k/description/

"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
	Input: nums = [1,1,1], k = 2
	Output: 2

Example 2:
	Input: nums = [1,2,3], k = 3
	Output: 2

Constraints:
	1 <= nums.length <= 2 * 10^4
	-1000 <= nums[i] <= 1000
	-10^7 <= k <= 10^7

Link: https://leetcode.com/problems/subarray-sum-equals-k/description/
"""

from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        subarray_count = 0
        sum_freq = {0: 1}
        prefix_sum = 0
        for num in nums:
            prefix_sum += num
            
            difference = prefix_sum - k
            
            if difference in sum_freq:
                
                subarray_count += sum_freq[difference]
            
            sum_freq[prefix_sum]= 1 + sum_freq.get(prefix_sum , 0)

        return subarray_count

def run_tests():
	sol = Solution()
	test_cases = [
		{"nums": [1, 1, 1], "k": 2, "expected": 2},
		# # This test case is intentionally wrong to demonstrate error logging:
		# {"nums": [1, 2, 3], "k": 3, "expected": 3},
		{"nums": [1, 2, 3], "k": 3, "expected": 2}
	]

	total_tests = len(test_cases)
	passed_tests = 0
	
	for test in test_cases:
		nums = test["nums"]
		k = test["k"]
		expected = test["expected"]
		result = sol.subarraySum(nums, k)
		if result != expected:
			print("A test case failed:")
			print(f"\tInput: nums = {nums}, k = {k}")
			print(f"\tExpected: {expected}")
			print(f"\tGot: {result}")
			print(f"Total tests passed before error: {passed_tests} out of {total_tests}")
			raise SystemExit("Test case failed. Stopping further execution.")
		else:
			passed_tests += 1
	
	print(f"All {passed_tests} test cases passed!")

if __name__ == "__main__":
	run_tests()
