class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        length = len(nums)
        left = 0
        right = 1

        while right < length:

            if nums[left] == nums[right]:
                right+=1
            
            if  right < length and nums[left] != nums[right]:
                left +=1
                nums[left] = nums[right]
            right +=1
        
        return left+1



        