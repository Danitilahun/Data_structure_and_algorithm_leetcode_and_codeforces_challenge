class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Approach : Binary search
        - When I see sorted and search -> Binary search comes to my mind
        - Even the array is rotated from mid point at least one part is sorted.
        - So if I can get to that sorted part I can do normal binary search so finding sorted part repeatedly
            will help to solve the problem
        
        # Algorithm 

        - Create low and high pointer, calculate mid 
        - Start by looking at the middle element of the array.
        - Check if this middle element is the target if yes, return its index immediately.
        - Now figure out which half of the array (left side or right side) is sorted.
        - If the left part is sorted:
            - Check if the target number falls within the range of that sorted part.
            - If it does, discard the right half and continue the search in the left part.
            - If it doesn’t, discard the left half and search in the right side.
        If the right part is sorted:
            - Do the same check if the target is in that sorted part.
            - If yes, discard the left side and search in the right.
            - If not, discard the right and continue with the left.
        - Repeat this process
        """

        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high)

            if nums[mid] == target:
                return mid
            
            if nums[mid] > nums[low]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[high] >= target > nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
        
        return -1