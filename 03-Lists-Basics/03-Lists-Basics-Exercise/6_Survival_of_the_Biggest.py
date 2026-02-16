nums = input().split(' ')
copy_nums = list(map(int, nums))
count = int(input())

for _ in range(count):
    current_min_element = min(copy_nums)
    nums.remove((str(current_min_element)))
    copy_nums.remove(current_min_element)

print(', '.join(nums))


# numbers = input().split()
# numbers_to_remove = int(input())
# nums = []
#
# for number in range(len(numbers)):
#     num = int(numbers[number])
#     nums.append(num)
#
# for i in range(numbers_to_remove):
#     nums.remove(min(nums))
#
# result_strings = []
#
# for n in nums:
#     result_strings.append(str(n))
#
# print(", ".join(result_strings))