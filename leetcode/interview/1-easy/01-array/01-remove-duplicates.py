nums = [0,0,1,1,1,2,2,3,3,4]
nums = [1,1,2]

k = 0

for i in range(1, len(nums)):
    if nums[i] != nums[k]:
        k += 1
        nums[k] = nums[i]

print(k+1)
print(nums)
