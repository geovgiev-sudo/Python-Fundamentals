# number_of_electrons = int(input())
# filled_shells = []
# electrons_left = 0
#
# for shell_position in range(1, number_of_electrons + 1):
#     electrons_to_fill = 2 * shell_position ** 2
#     electrons_left = number_of_electrons - sum(filled_shells)
#     if electrons_left == 0:
#         break
#     if electrons_to_fill >= electrons_left:
#         filled_shells.append(electrons_left)
#         break
#     filled_shells.append(electrons_to_fill)
#
# print(filled_shells)



number_of_electrons = int(input())
shells = []
number_of_shell = 0
while number_of_electrons > 0:
    number_of_shell += 1
    max_electrons_in_current_shell = 2 * number_of_shell ** 2
    if number_of_electrons >= max_electrons_in_current_shell:
        shells.append(max_electrons_in_current_shell)
    else: # number_of_electrons < max_electrons_in_current_shell
        shells.append(number_of_electrons)
    number_of_electrons -= max_electrons_in_current_shell
print(shells)