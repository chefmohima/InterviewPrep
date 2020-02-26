# Find missing number in an array
# How do you find the missing number in a given integer array of 1 to 100?
# calculate sum of all numbers in the range, subtract the actual sum of numbers in the list
def find_missing_number(start, end, nums):
    sum_without_missing_num = sum(range(start, end+1))
    actual_sum = sum(nums)
    missing_num = sum_without_missing_num - actual_sum
    return missing_num
