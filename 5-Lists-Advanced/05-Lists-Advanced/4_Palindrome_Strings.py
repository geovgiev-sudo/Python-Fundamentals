strings = input().split()
palindrome = input()
palindrome_count = 0

found_palindromes = [word for word in strings if word == "".join(reversed(word))]
palindrome_count = found_palindromes.count(palindrome)

print(found_palindromes)
print(f"Found palindrome {palindrome_count} times")

# strings = input().split()
# palindrome = input()
# found_palindromes = []
# palindrome_count = 0
#
# for word in strings:
#     if word == word[::-1]:
#         found_palindromes.append(word)
#         if word == palindrome:
#             palindrome_count += 1
#
# print(found_palindromes)
# print(f"Found palindrome {palindrome_count} times")
#
