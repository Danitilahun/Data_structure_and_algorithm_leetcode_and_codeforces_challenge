class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        answer = [0]* n

        for i in range(n):
            count = 0
            for j in range(i,-1,-1):
                for k in range(i,-1,-1):
                    if A[j] == B[k]:
                        count+=1
            answer[i] = count
        
        return answer

