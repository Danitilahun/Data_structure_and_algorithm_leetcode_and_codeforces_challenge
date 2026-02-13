class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        total_tank = 0
        start_index = 0
        n = len(gas)
        for index in range(n):
            total_tank += gas[index % n] - cost[index % n]
            
            if total_tank < 0:
                total_tank = 0
                start_index = index + 1
        
        return start_index if start_index < n else -1