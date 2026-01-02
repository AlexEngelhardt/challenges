# Given a 32-bit unsigned integer n, reverse the bits of the binary representation of n and return the result.
#
# Example 1:
#
# Input: n = 00000000000000000000000000010101
#
# Output:    2818572288 (10101000000000000000000000000000)
#
# Explanation: Reversing 00000000000000000000000000010101, which represents the unsigned integer 21, gives us 10101000000000000000000000000000 which represents the unsigned integer 2818572288.
#

class Solution:
    def reverseBits(self, n: int) -> int:
        n_bin = bin(n)[2:]
        n_bin = "0" * (32 - len(n_bin)) + n_bin
        res = n_bin[::-1]
        return int(res, 2)


def test_reverse_bits():
    assert Solution().reverseBits(21) == 2818572288
