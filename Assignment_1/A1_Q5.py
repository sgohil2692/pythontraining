def list_count_4(nums):
  count = 0  
  for num in nums:
    if num == 4:
      count = count + 1

  return count

print(list_count_4([1,2,3,4,5,8,4,4,4,4,3,2,3,2,5,6]))