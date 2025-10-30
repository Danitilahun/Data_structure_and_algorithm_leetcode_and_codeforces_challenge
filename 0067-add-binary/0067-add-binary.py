class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_len = len(a) - 1
        b_len = len(b) - 1
        carrier = 0
        answer = ""
        while (a_len >= 0 or b_len >= 0 or carrier):
            summation = carrier

            if(a_len >= 0): summation += int(a[a_len])
            if(b_len >= 0): summation += int(b[b_len])

            answer += str(summation % 2)
            carrier = summation // 2

            a_len -=1
            b_len -=1
        
        return answer[::-1]