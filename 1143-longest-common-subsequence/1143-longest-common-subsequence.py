class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        text_1_length = len(text1)
        text_2_length = len(text2)

        dp = [[-1 for _ in range(text_2_length)] for _ in range(text_1_length)]

        def CommonSubsequenceLength(index1, index2):
            if index1 >= text_1_length or index2 >= text_2_length: return 0
            if dp[index1][index2] != -1: return dp[index1][index2]

            match = 0
            not_match = 0
            if text1[index1] == text2[index2]:
                match = 1 + CommonSubsequenceLength(index1+1,index2+1)
            else:
                not_match = max(CommonSubsequenceLength(index1+1,index2) , CommonSubsequenceLength(index1,index2 + 1))

            dp[index1][index2] = max(match, not_match)

            return dp[index1][index2]
        
        return CommonSubsequenceLength(0,0)