class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left=0
        right=int(c**0.5)

        # Why limit 'a' (and 'b') to sqrt(c)? Proof by Contradiction:
        # Assume a > sqrt(c). Then a^2 > c.
        # Since b^2 >= 0, it follows that a^2 + b^2 > c, which contradicts a^2 + b^2 = c.
        # By symmetry (since a^2 + b^2 is the same as b^2 + a^2), this logic applies to 'b' as well.
        # Therefore, neither 'a' nor 'b' can exceed sqrt(c).
        
        while left<=right:
            cur=(left*left + right*right)
            if cur>c:
                right-=1
            elif cur<c:
                left+=1
            else:
                return True
        return False