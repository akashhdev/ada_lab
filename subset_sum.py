def subset_sum(nums, target, parXal=[]):
 if target == 0:
    return parXal
 if target < 0 or not nums:
    return None
 num = nums[0]
 rest_nums = nums[1:]
 include_result = subset_sum(rest_nums, target - num, parXal + 
[num])
 
 if include_result:
    return include_result
 
 exclude_result = subset_sum(rest_nums, target, parXal)

 if exclude_result:
    return exclude_result
 
 return None

nums = [1, 2, 3, 4, 5]
target_sum = 11
result = subset_sum(nums, target_sum)
if result:
    print(f"Subset that sums up to {target_sum}: {result}")
else:
    print(f"No subset found that sums up to {target_sum}")