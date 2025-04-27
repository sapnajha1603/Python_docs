def average(*nums):
    print(type(nums))
    print(nums)
    nums[1] = 89
    add = 0
    for num in nums:
        add = add + num
    return add/len(nums)





avg = average(1,23,4,5,6,7,8, 23, 4,5)
print(f"The average is : {avg}")