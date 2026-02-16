sequence_of_numbers = input().split()
sequence_int = list((map(int, sequence_of_numbers)))
left_car_time = 0
right_car_time = 0
total_time = 0
winner = ""

middle_index = len(sequence_int) // 2

for left in range(middle_index):
    if sequence_int[left] == 0:
        left_car_time *= 0.80
    left_car_time += sequence_int[left]

for right in range(len(sequence_int) - 1, middle_index, - 1):
    if sequence_int[right] == 0:
        right_car_time *= 0.80
    right_car_time += sequence_int[right]

if left_car_time < right_car_time:
    winner = "left"
    total_time = left_car_time
elif right_car_time < left_car_time:
    winner = "right"
    total_time = right_car_time


print(f"The winner is {winner} with total time: {total_time:.1f}")
