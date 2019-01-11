def odd_product(nums):
  for i in range(len(nums)):
    for j in range(len(nums)):
      if  i != j:
        product = nums[i] * nums[j]
        if product & 1:
          return True
          return False
          
dt1 = [1, 3, 5, 7, 9]
dt2 = [10, 20, 30, 40, 50]
dt3 = [2, 4, 1, 6, 8]
print(dt1, odd_product(dt1));
print(dt2, odd_product(dt2));
print(dt3, odd_product(dt3));