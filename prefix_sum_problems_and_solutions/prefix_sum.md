# Prefix Sum Pattern

## What are Prefix Sums?
- **Prefix sums** are a technique for handling cumulative information in arrays.
- A prefix sum array `P` of an original array `A` is constructed so that:

	```
	P[i] = A[0] + A[1] + ... + A[i - 1]
	```
	(or `P[i]` might sometimes represent the sum of elements up to and including `A[i]`, depending on your indexing choice).

## Typical Steps
1. Compute the prefix sum array.
2. Use the prefix sums to answer queries about subarray sums or to detect subarrays meeting certain conditions.

## Common Applications
- **Range Sum Queries:** Quickly determine the sum of any segment in O(1) time after O(n) preprocessing.
- **Subarray Sum Problems:** Find subarrays that sum to a particular target (commonly used with a hash map to manage frequencies of prefix sums).

## Complexity
- **Time Complexity:** O(n) to build the prefix sums. Each range query or subarray sum check is O(1).
- **Space Complexity:** O(n) to store the prefix sums.

For more practice, check the 
[LeetCode Problem Set](https://dilipkumar.medium.com/prefix-sum-coding-pattern-1f3a12be5038).