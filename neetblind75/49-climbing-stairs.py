# You are given an integer n representing the number of steps to reach the top of a staircase. You can climb with either 1 or 2 steps at a time.
#
# Return the number of distinct ways to climb to the top of the staircase.
#
# Example 1:
#
# Input: n = 2
#
# Output: 2
#
# Explanation:
#
#     1 + 1 = 2
#     2 = 2
#
# Example 2:
#
# Input: n = 3
#
# Output: 3
#
# Explanation:
#
#     1 + 1 + 1 = 3
#     1 + 2 = 3
#     2 + 1 = 3
#
# Constraints:
#
#     1 <= n <= 30
#
# You should aim for a solution as good or better than O(n) time and O(n) space, where n is the number of steps. 

class Solution:
    def __init__(self):
        self.cache = [1, 1, 2]  # n=0 => ways=1. etc.
    def climbStairs(self, n: int) -> int:
        # Uh, this is just the Fibonacci series!
        if len(self.cache) > n:
            return self.cache[n]
        else:
            res = self.climbStairs(n-1) + self.climbStairs(n-2)
            assert len(self.cache) == n
            self.cache.append(res)  # In this case the cache is always exactly 1 item too short (see previous `assert`), so we can just append the current result
            return res

def test_climb_stairs():
    sol = Solution()
    assert sol.climbStairs(2) == 2
    assert sol.climbStairs(3) == 3
    assert sol.climbStairs(38) == 63245986
