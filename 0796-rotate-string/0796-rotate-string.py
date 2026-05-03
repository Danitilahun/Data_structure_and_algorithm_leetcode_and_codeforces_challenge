class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(goal)
        if n != len(s):
            return False

        for index in range(n):
            if goal[index] == s[0]:
        
                rotated = goal[index:] + goal[:index]
                if rotated == s:
                    return True

        return False