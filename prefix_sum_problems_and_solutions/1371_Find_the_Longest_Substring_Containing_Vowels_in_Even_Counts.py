"""
1371. Find the Longest Substring Containing Vowels in Even Counts
https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/

### Problem Statement:
Given a string `s`, return the size of the longest substring where each vowel ('a', 'e', 'i', 'o', 'u') 
appears an even number of times.

### Examples:
**Example 1:**
Input: s = "eleetminicoworoep"
Output: 13
Explanation: The longest valid substring is "leetminicowor" where e, i, and o appear twice.

**Example 2:**
Input: s = "leetcodeisgreat"
Output: 5
Explanation: The longest substring is "leetc" which contains two e's.

**Example 3:**
Input: s = "bcbcbc"
Output: 6
Explanation: The entire string is valid since no vowels appear.

### Constraints:
- 1 <= s.length <= 5 × 10^5
- s contains only lowercase English letters.

### Techniques Used:
1. **Bit Manipulation (Bit Masking)** → Each vowel is represented as a bit in a binary mask, toggled when encountered.
2. **Prefix Sum Technique with Hashing** → Stores the first occurrence of each mask to compute substring lengths in O(1).
3. **XOR for Parity Tracking** → Tracks whether each vowel appears an even or odd number of times.
"""

class Solution:
	def findTheLongestSubstring(self, s: str) -> int:
		n = len(s)
		vowels = 'aeiou'
		res = 0
		mask = 0
		mask_to_idx = {0: -1}

		for idx in range(n):
			char = s[idx]
			if char in vowels:
				bit_position = (1 + ord(char) - ord('a'))
				mask ^= bit_position

			if mask in mask_to_idx:
				res = max(res, idx - mask_to_idx[mask])
			else:
				mask_to_idx[mask] = idx

		return res
