class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        left = 0
        k_count = 0
        answer = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                k_count +=1
            
            while k_count > k:
                if nums[left] == 0:
                    k_count -=1
                left +=1
            
            answer = max(answer, right - left + 1)
        
        return answer