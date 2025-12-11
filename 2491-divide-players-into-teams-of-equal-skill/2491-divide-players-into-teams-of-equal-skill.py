class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        length = len(skill)
        left = 0
        right = length - 1
        answer = 0
        while left < right:
            sum_ = skill[left] + skill[right]
            sum_next = skill[left+1] + skill[right -1]
            if sum_ != sum_next:
                return -1
            
            answer += (skill[left] * skill[right])

            left +=1
            right -=1
        
        return answer