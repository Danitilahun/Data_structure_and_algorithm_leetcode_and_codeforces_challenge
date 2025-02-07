# 325. Maximum Size Subarray Sum Equals k 

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
