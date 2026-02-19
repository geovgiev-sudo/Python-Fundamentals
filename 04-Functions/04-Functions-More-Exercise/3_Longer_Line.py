from math import floor

def dist2_to_center(x, y):
    return x * x + y * y


def line_len2(x1, y1, x2, y2):
    dx = x1 - x2
    dy = y1 - y2
    return dx * dx + dy * dy


def order_points_by_center(x1, y1, x2, y2):
    if dist2_to_center(x1, y1) <= dist2_to_center(x2, y2):
        return (x1, y1), (x2, y2)
    return (x2, y2), (x1, y1)


def floor_point(p):
    return floor(p[0]), floor(p[1])


def main(x1, y1, x2, y2, x3, y3, x4, y4):
    len1 = line_len2(x1, y1, x2, y2)
    len2 = line_len2(x3, y3, x4, y4)

    if len1 >= len2:
        p1, p2 = order_points_by_center(x1, y1, x2, y2)
    else:
        p1, p2 = order_points_by_center(x3, y3, x4, y4)

    p1 = floor_point(p1)
    p2 = floor_point(p2)

    print(f"({p1[0]}, {p1[1]})({p2[0]}, {p2[1]})")


x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())
x_3 = float(input())
y_3 = float(input())
x_4 = float(input())
y_4 = float(input())

main(x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4)