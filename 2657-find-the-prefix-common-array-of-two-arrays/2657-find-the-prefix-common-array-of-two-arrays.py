class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        answer = [0]* n
        visited = {i:0 for i in range(1,n+1)}
        count = 0
        for i in range(n):
            visited[A[i]] +=1
            visited[B[i]] +=1
 
            if (A[i] == B[i]):
                count += 1
            else:
                if (visited[A[i]] == 2):
                    count += 1
                if (visited[B[i]] == 2):
                    count += 1
            
            
            answer[i] = count
        
        return answer

