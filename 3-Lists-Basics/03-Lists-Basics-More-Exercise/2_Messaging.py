# МОЕТО РЕШЕНИЕ - 100/100 В Judge

# sequence = input().split()
# sequence_int = []
# for num in sequence:
#     sequence_int.append(num)
# text_sequence = list(input())
# message = ""
#
# for i in range(len(sequence_int)):
#     single_number = str(sequence_int[i])
#     index = 0
#     for num in single_number:
#         index += int(num)
#
#     if index >= len(text_sequence):
#         new_index = index - len(text_sequence)
#         message += text_sequence[new_index]
#         text_sequence.remove(text_sequence[new_index])
#     else:
#         message += text_sequence[index]
#         text_sequence.remove(text_sequence[index])
#
# print(message)

# Подобрено решение
#
sequence = input().split()
sequence_int = list((map(int, sequence)))
text_sequence = list(input())
message = ""

for i in range(len(sequence_int)):
    single_number = str(sequence_int[i])
    index = 0
    for num in single_number:
        index += int(num)

    if index >= len(text_sequence):
        index %= len(text_sequence)

    message += text_sequence[index]
    text_sequence.pop(index) # .pop премахва конкретния индекс
print(message)



# sequence_of_numbers = input().split()
# text = input()
#
# text_list = list(text)
# message = ""
#
# for number in sequence_of_numbers:
#     digit_sum = 0
#
#     for digit in number:
#         digit_sum += int(digit)
#
#     index = digit_sum % len(text_list)
#     message += text_list[index]
#     text_list.pop(index)
#
# print(message)








# list_numbers = input().split(' ')
# message = input()
# message_list = []
#
# for numbers in list_numbers:
#     current_sum = 0
#     for integer_numbers in numbers:
#         current_sum += int(integer_numbers)
#
#     current_sum %= len(message)
#
#     message_list.append(message[current_sum])
#     message = message.replace(message[current_sum], '', 1)
#
# print(''.join(message_list))