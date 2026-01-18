class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
    
        length = len(nums)
        
        if length == 1 or nums[0] != nums[1]:
            return nums[0]
        
        if nums[length - 1] != nums[length - 2]:
            return nums[length - 1]

        low = 1
        high = length - 2
        while low <= high:
            mid = (low + high)//2

            if nums[mid-1] != nums[mid] and nums[mid+1] != nums[mid]:
                return nums[mid]
            
            if mid%2 == 0: 
                if nums[mid+1] == nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
            elif mid%2 != 0:
                if nums[mid+1] == nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
        return -1

