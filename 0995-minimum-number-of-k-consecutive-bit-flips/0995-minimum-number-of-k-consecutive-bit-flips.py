class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:

        """
        nums = [0,1,0,0,1,0]
        k= 4
        """
        
        count = 0

        n = len(nums)
        flips_count = [0] * (n+1)
        current_flips_count = 0
        flip_total = 0
        for ind in range(n-k+1):
            
            current_flips_count+=flips_count[ind]

            flip = current_flips_count % 2
            
            if (nums[ind] == 0 and flip == 0) or (nums[ind] == 1 and flip == 1):
                flips_count[ind]+=1
                flips_count[ind+k] =-1
                flip_total +=1 
                current_flips_count+=1


        for ind in range(1,n):
            flips_count[ind]+=flips_count[ind - 1]
        
        for ind in range(n):
            if flips_count[ind]%2:
                nums[ind] = 0 if nums[ind] == 1 else 1
        
        impossiblity_check = any(nums[ind]==0 for ind in range(n))

        return flip_total if impossiblity_check == False else -1


