class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        
        count = 0

        n = len(nums)
        flips_count = [0] * (n+1)
        current_flips_count = 0
        flip_total = 0
        impossiblity_check = False

        for ind in range(n):

            
            current_flips_count+=flips_count[ind]

            flip = current_flips_count % 2
            
            if ind + k <= n and  ((nums[ind] == 0 and flip == 0) or (nums[ind] == 1 and flip == 1)):
                flips_count[ind]+=1
                flips_count[ind+k] =-1
                flip_total +=1 
                current_flips_count+=1
            
            if current_flips_count%2:
                nums[ind] = 0 if nums[ind] == 1 else 1
            
            if nums[ind] == 0: impossiblity_check = True


        return flip_total if impossiblity_check == False else -1


