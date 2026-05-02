class Solution:
    def rotatedDigits(self, n: int) -> int:
        count = 0
        valid_nums = {2,5,6,9}
        invalid_nums = {3,4,7}
        memo = {}
        for num in range(2,n+1):
            valid = False

            if num in invalid_nums:
                continue
            
            orginal_num = num

            while num:
                 
                digit = num%10
                if digit in valid_nums:
                    valid = True
                    prefix= num // 10
                    if prefix in memo:
                        break
                elif digit in invalid_nums:
                    valid = False
                    break
                num //= 10

            
            if valid:
                memo[orginal_num//10]= True
                count += 1
        
        return count
