class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        lenght = len(people)
        if lenght == 1:
            return 1
        
        left = 0
        right = lenght -1
        boat = 0

        while left < right:
            weight = people[left] + people[right]

            if weight <= limit:
                left+=1
            
            right -=1
            boat +=1
        return boat if left != right else boat+1
