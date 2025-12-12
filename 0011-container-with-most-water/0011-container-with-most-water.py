class Solution:
    def maxArea(self, height: List[int]) -> int:
        lenght = len(height)
        left = 0
        right = lenght - 1

        answer = 0

        while left < right:

            mini = min(height[left],height[right])

            answer = max(answer, mini * (right - left))

            if height[left] > height[right]:
                right -=1
            else:
                left +=1
        
        return answer

