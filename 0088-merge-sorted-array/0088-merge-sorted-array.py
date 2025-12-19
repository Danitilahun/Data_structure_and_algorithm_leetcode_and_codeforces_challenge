class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        num1_left = m - 1
        num1_right = m + n - 1
        num2_right = n - 1

        while num1_right >=0 and num2_right>=0:
            if num1_left >= 0 and nums1[num1_left] > nums2[num2_right]:
                nums1[num1_right] = nums1[num1_left]
                num1_left -=1
            else:
                nums1[num1_right] = nums2[num2_right]
                num2_right -=1
            num1_right -=1
        
