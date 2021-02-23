from display import *
from draw import *
from math import pi, dist
import random
s = new_screen()
c = [ 255, 255, 255 ]

def draw_snowflake(start_one, start_two, end_one):
    theta = pi / 3
    point_one = [start_one, start_two]
    point_two = [start_one, end_one]
    for _ in range(6):
        draw_line(point_one[0], point_one[1], point_two[0], point_two[1], s, c)
        point_one = rotate_point(point_one, theta, start_one, start_two)
        point_two = rotate_point(point_two, theta, start_one, start_two)
def draw_nucler_plant(start_one, start_two, end_one):
    p = [0, 0, 0]
    # base
    draw_line(start_one - 30, start_two, start_one - 10, start_two + 30, s, p)
    draw_line(start_one + 50, start_two, start_one + 30, start_two + 30, s, p)
    # stem
    draw_line(start_one - 10, start_two + 30, start_one - 10, end_one, s, p)
    draw_line(start_one + 30, start_two + 30, start_one + 30, end_one, s, p)

    #top
    draw_line(start_one - 10, end_one, start_one - 20, end_one + 10, s, p)
    draw_line(start_one + 30, end_one, start_one + 40, end_one + 10, s, p)
    draw_line(start_one - 20, end_one + 10, start_one + 40, end_one + 10, s, p)

    p = [148, 156, 161]
    #smoke
    for i in range(0, 10, 2):
        for j in range(0, 10):
            plot(s, p, start_one + 10 + j, end_one + 15 + i)
            plot(s, p, start_one + 10 - j, end_one + 15 + i)
    



draw_nucler_plant(XRES/4, 0, (2 * YRES) / 5)
draw_nucler_plant(XRES/2, 0, (2 * YRES) / 5)
draw_nucler_plant(3 * XRES / 4, 0, (2 * YRES) / 5)



for i in range(200):
    start_one = random.randint(2, XRES)
    start_two = random.randint(YRES/2, YRES)
    end_one = start_two + random.randint(3, 5)
    draw_snowflake(start_one, start_two, end_one)

for i in range(10):
    draw_line(0, i, XRES, i, s, c)
    

    












# #octants 1 and 5
# draw_line(0, 0, XRES-1, YRES-1, s, c)
# draw_line(0, 0, XRES-1, YRES / 2, s, c) 
# draw_line(XRES-1, YRES-1, 0, YRES / 2, s, c)

# #octants 8 and 4
# c[BLUE] = 255;
# draw_line(0, YRES-1, XRES-1, 0, s, c);  
# draw_line(0, YRES-1, XRES-1, YRES/2, s, c);
# draw_line(XRES-1, 0, 0, YRES/2, s, c);

# #octants 2 and 6
# c[RED] = 255;
# c[GREEN] = 0;
# c[BLUE] = 0;
# draw_line(0, 0, XRES/2, YRES-1, s, c);
# draw_line(XRES-1, YRES-1, XRES/2, 0, s, c);

# #octants 7 and 3
# c[BLUE] = 255;
# draw_line(0, YRES-1, XRES/2, 0, s, c);
# draw_line(XRES-1, 0, XRES/2, YRES-1, s, c);

# #horizontal and vertical
# c[BLUE] = 0;
# c[GREEN] = 255;
# draw_line(0, int(YRES/2), XRES-1, int(YRES/2), s, c);
# draw_line(int(XRES/2), 0, int(XRES/2), int(YRES-1), s, c);


display(s)
save_ppm(s, 'binary.ppm')
save_ppm_ascii(s, 'ascii.ppm')
save_extension(s, 'img.png')
