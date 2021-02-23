from display import *
from math import inf, cos, sin  # inf --> infinity


def rotate_point(point, theta, origin_x, origin_y):
    point[0], point[1] = (
        ((point[0] - origin_x) * cos(theta)) - ((point[1] - origin_y) * sin(theta))
    ) + origin_x, ((point[1] - origin_y) * cos(theta)) + ((point[0] - origin_x) * sin(theta)) + origin_y
    return point


def draw_line(x0, y0, x1, y1, screen, color):
    temp = x0
    x0, x1 = min(x0, x1), max(x0, x1)
    if x0 != temp:
        y0, y1 = y1, y0
    if (x0 == x1):
        temp = y0
        y0, y1 = min(y0, y1), max(y0, y1)
        if y0 != temp:
            x0, x1 = x1, x0
    dx = x1 - x0
    dy = y1 - y0
    A = dy
    B = -dx
    x = x0
    y = y0
    if dx == 0:  # vertical line
        d = A + (2 * B)  # equivalent to 2 * f(x0 + 1/2, y0 + 1)
        while y <= y1:
            plot(screen, color, x, y)
            if d < 0:
                d += 2 * (A + B)
                x += 1
            else:
                d += 2 * B
            y += 1
    elif dy / dx >= 0 and dy / dx <= 1:  # Octant 1 and 5: (0 < m <= 1)
        d = (2 * A) + B  # equivalent to 2 * f(x0 + 1, y0 + 1/2)
        while x <= x1:
            plot(screen, color, x, y)
            if d < 0:
                d += 2 * A
            else:
                d += 2 * (A + B)
                y += 1
            x += 1
    elif (dy / dx) > 1 and (dy / dx) < inf:  # Octants 2 and 6: (1 < m < inf)
        d = A + (2 * B)  # equivalent to 2 * f(x0 + 1/2, y0 + 1)
        while y <= y1:
            plot(screen, color, x, y)
            if d < 0:
                d += 2 * (A + B)
                x += 1
            else:
                d += 2 * B
            y += 1
    elif dy / dx < 0 and dy / dx >= -1:  # Octants 4 and 8 (-1 <= m < 0)
        d = (2 * A) - B  # equivalent to 2 * f(x0 + 1, y0 - 1/2)
        while x <= x1:
            plot(screen, color, x, y)
            if d < 0:
                d += 2 * (A - B)
                y -= 1
            else:
                d += 2 * A
            x += 1
    elif dy / dx < -1 and dy / dx > -inf:  # Octants 3 and 7 (-inf < m < -1)
        d = A - (2 * B)
        while y >= y1:
            plot(screen, color, x, y)
            if d < 0:
                d += 2 * -B
            else:
                d += 2 * (A - B)
                x += 1
            y -= 1