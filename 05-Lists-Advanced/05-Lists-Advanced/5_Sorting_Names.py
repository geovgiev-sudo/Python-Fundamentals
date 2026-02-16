names_list = input().split(", ")

sorted_names = sorted(names_list)
final_sorted = sorted(sorted_names, key=len, reverse=True)

# print(sorted_names)
print(final_sorted)

# names_list.sort()
# names_list.sort(key=len, reverse=True)
# print(names_list)



# names_list = input().split(", ")
# sorted_names = sorted(names_list, key= lambda x: (-len(x), x))
#
# print(sorted_names)