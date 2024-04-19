
def find_missing_number(nums):
    n = len(nums)
    total_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return total_sum - actual_sum

def rotate_array(nums, k):
    k %= len(nums)
    nums[:] = nums[-k:] + nums[:-k]

def remove_duplicates(nums):
    if not nums:
        return 0
    
    index = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[index] = nums[i]
            index += 1
    
    return index

def merge_sorted_array(num1, num2):
    num1.extend(num2)
    num1.sort()

def max_subarray_sum(nums):
    max_sum = current_sum = nums[0]
    
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum

nums_missing_number = [5, 2, 0, 3, 1]
print(find_missing_number(nums_missing_number))

nums_rotate_array = [1, 2, 3, 4, 5]
rotate_array(nums_rotate_array, 2)
print(nums_rotate_array)

nums_remove_duplicates = [1, 1, 2, 2, 3, 4, 5 ,5]
print(remove_duplicates(nums_remove_duplicates))

num1_merge_sorted_array = [1 ,2 ,3]
num2_merge_sorted_array = [2 ,5 ,6]
merge_sorted_array(num1_merge_sorted_array,num2_merge_sorted_array)
print(num1_merge_sorted_array)

nums_max_subarray_sum = [-2 ,-1 ,-3 ,4 ,-1 ,2 ,1 ,-5 ,4]
print(max_subarray_sum(nums_max_subarray_sum))



