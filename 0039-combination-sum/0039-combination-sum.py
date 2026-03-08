class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n= len(candidates)
        answer = []
        def TargetCombinations(index, target, arr=[]):

            if index >= n: return

            if target == 0:
                answer.append(arr.copy())
                return

            if target < 0: return 

            # Pick
            arr.append(candidates[index])
            pick = TargetCombinations(index, target - candidates[index], arr)

            # Not Pick
            arr.pop()
            not_pick = TargetCombinations(index + 1, target, arr)

        TargetCombinations(0,target)
        return answer