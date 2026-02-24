from math import floor
def main(first_x, first_y, second_x, second_y):

    first_distance = first_x ** 2 + first_y ** 2
    second_distance = second_x ** 2 + second_y ** 2

    if first_distance <= second_distance:
        return floor(first_x), floor(first_y)
    return floor(second_x), floor(second_y)

first_dot_x = float(input())
first_dot_y = float(input())
second_dot_x = float(input())
second_dot_y = float(input())

result = main(first_dot_x, first_dot_y, second_dot_x, second_dot_y)

print(result)








import math


def get_distance(_x1, _y1, _x2, _y2):
    return math.sqrt(math.pow(_x2 - _x1, 2.0) + math.pow(_y2 - _y1, 2.0))


x1 = math.floor(float(input()))
y1 = math.floor(float(input()))
x2 = math.floor(float(input()))
y2 = math.floor(float(input()))

dist1 = get_distance(x1, y1, 0, 0)
dist2 = get_distance(x2, y2, 0, 0)

if dist1 <= dist2:
    print(f"({x1}, {y1})")
else:
    print(f"({x2}, {y2})")