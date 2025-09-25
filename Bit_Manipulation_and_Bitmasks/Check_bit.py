"""
In a given integer N, check whether the ith bit is set or not.

Input Format
    First and only line of input contains N and i.

Constraints
    0 <= N <= 10^9
    0 <= i <= 30

Output Format
    Print "true" if ith bit is set in the given integer N, "false" otherwise.

Inputcopy	Outputcopy
10 1        true

Explanation 0

The binary form of 10 is: 1010. So the 1st bit in 10 is set. Note that LSB bit is referred as 0th bit.
"""


# Constraint : 0 <= N <= 10^9 and 0 <= i <= 30
# Input : N and i
# Output : Boolean
# Specific assumptions : 
    # N is a non-negative integer within the given range.
    # i is a valid bit position for a 32-bit integer.
    # The bit positions are counted from the least significant bit (rightmost, 0th position).

def check_ith_bit_set(N : int, i : int)-> bool:
    
    mask = 1<<i
    print(mask, N)
    
    return (N & mask) != 0

print(check_ith_bit_set(10,1))