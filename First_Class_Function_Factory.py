def factory(x):
    def multiply_by_number(nums):
        for num in range(0, len(nums)):
            nums[num] = nums[num] * x
        return nums
    return multiply_by_number




print(factory(3)([1, 2, 3]))