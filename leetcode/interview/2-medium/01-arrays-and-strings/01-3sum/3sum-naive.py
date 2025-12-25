#nums = [0,1,1]
#nums = [0, 0, 0]
nums = [-1,0,1,2,-1,4]

result = set()

for i in range(len(nums)-2):
    for j in range(i+1, len(nums)-1):
        for k in range(j+1, len(nums)):
            # print(f"i {i} j {j} k {k}")
            if nums[i] + nums[j] + nums[k] == 0:
                # print([nums[i],nums[j],nums[k]])
                result.add(tuple(sorted([nums[i],nums[j],nums[k]])))

result = list(x for x in result)
print(result)
