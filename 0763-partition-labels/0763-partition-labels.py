from collections import Counter
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        letters = Counter(s)
        tracker = {}
        left = 0
        lenght = len(s)
        answer = []

        for right in range(lenght):
            tracker[s[right]] = tracker.get(s[right],0) + 1
            difference = 0

            for item in tracker:
                difference += (letters[item] - tracker[item])
            if difference == 0:
                answer.append(right - left + 1)
                left = right + 1
        
        return answer
        