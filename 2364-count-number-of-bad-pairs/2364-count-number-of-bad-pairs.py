class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        
        total_good_pairs = 0
        n = len(nums)
        total_pairs = (n * (n-1)) // 2
        mapp = {}
        for i in range(n):
            check = i - nums[i]
            if check in  mapp:
                total_good_pairs += mapp[check]
            
            mapp[check] = mapp.get(check,0) + 1
        total_bad_pairs = total_pairs - total_good_pairs
        return total_bad_pairs