class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if k%n ==0:
            return nums
        k = k % n

        def reverse(nums,start,end):
            while start< end:
                nums[start],nums[end] = nums[end],nums[start]
                start+=1
                end-=1
        
        start = 0
        end = n - 1
        reverse(nums,start,end)

        start = 0
        end = k - 1
        reverse(nums,start,end)

        start = k
        end = n - 1
        reverse(nums,start,end)

        return nums