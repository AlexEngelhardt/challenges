# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
#
#  
#
# Example 1:
#
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
#
# Example 2:
#
# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
#
#  
#
# Constraints:
#
#     1 <= nums.length <= 105
#     -231 <= nums[i] <= 231 - 1
#     0 <= k <= 105
#
#  
#
# Follow up:
#
#     Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
#     Could you do it in-place with O(1) extra space?
#



nums = [1,2,3,4,5,6,7]
k = 3
# expected result = [5,6,7,1,2,3,4]

# try k=2 too!
# expected result = [6,7,1,2,3,4,5]

# not in-place:
out = [nums[(i-k) % len(nums)] for i in range(len(nums))]
print(out)

# for i in range(len(nums)):
#     nums[i] = out[i]

# in-place:

# cyclic dependencies: you must run through the array more often:
# if len % k == 0, you must run through k times. Else 1 time.

def right(arr_len, base_idx, step):
    return (arr_len + base_idx - step) % arr_len

print("7, from=0, step=3 (expect: 4) " + str(right(7, 0, 3)))
print("7, from=5, step=1 (expect: 4) " + str(right(5, 0, 1)))

# currently only the LAST number fails. I should start with buf = nums[0], nums[3] = buf, then go from there
# (will need two bufs though, or an extra variable for num[0])

if len(nums) % k:  # the easy case

    buf = 0
    idx = 0
    for i in range(len(nums)):
        print(f"i:{i}, idx:{idx}")
        buf = nums[idx]
        print(f"replacing nums[IDX] with nums[IDX2]")
        nums[idx] = nums[right(len(nums), idx, k)]
        idx = right(len(nums), idx, k)

print(nums)

# else:  # the hard case
