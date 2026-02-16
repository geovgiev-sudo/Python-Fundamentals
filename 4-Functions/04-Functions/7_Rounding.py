sequence = input().split()
sequence_int = []

for num in range(len(sequence)): # Вариант 1 за преобразуване
    sequence_int.append(round(float(sequence[num]))) # Тук трябва да взема по индекс

# for num in sequence: # Вариант 2 за преобразуване
    #sequence_int.append(abs(float(num))) # Тук директно взимам num

print(sequence_int)