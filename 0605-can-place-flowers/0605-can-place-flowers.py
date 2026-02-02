class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
        - What rule must never be violated? -> "Flowers cannot be planted in adjacent plots."

        Algorithm:
        - Iterate over the flowerbed array
        - If the current value is 1 skip it
        - if the current value is 0 check
            - If it has adjacent element in the right, it should be 0 or does not exist
            - If it has adjacent element in the left, it should be 0 or does not exist
        - If both condition got satisfied, decreaase n count by 1 and set the index value as 1(plotted)
        - if n becomes zero while decreased return True
        - return False if n does not becomes zero
        """
        length = len(flowerbed)
        for index in range(length):
            if flowerbed[index] != 1:
                left_empty = (index == 0) or (flowerbed[index - 1] == 0)
                right_empty = left_empty and ((index == length - 1) or (flowerbed[index+1] == 0))
                
                if left_empty and right_empty:
                    n-=1
                    flowerbed[index] = 1
                    if n <= 0:
                        return True
        return n == 0
                

                


