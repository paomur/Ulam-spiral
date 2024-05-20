import numpy as np
import tifffile
from sympy import isprime
width, height = 2 ** 10, 2 ** 10
data = np.zeros((height, width), dtype=np.uint8)


def is_Mercen(x):
    if x == 2:
        return True
    if x < 2:
        return False
    x = x ** 0.5
    return is_Mercen(x)


center_x, center_y = width // 2, height // 2

x, y = center_x, center_y
dx, dy = 0, 1
count = 0
count_snail_step = 1
snail_direction = -1  # -1 - Right, 0 - Up, 1 - Left, 2 - Down
count_snail_step_finished = 0
count_snail_megastep_finished = 0
for i in range(1, width * height):
    try:
        count += 1
        chis = count
        if isprime(chis):
            data[y, x] = 0
        else:
            data[y, x] = 255
        count_snail_step_finished += 1
        if snail_direction == -1:
            dx, dy = 1, 0
        elif snail_direction == 0:
            dx, dy = 0, 1
        elif snail_direction == 1:
            dx, dy = -1, 0
        elif snail_direction == 2:
            dx, dy = 0, -1
        if count_snail_step_finished == count_snail_step:
            count_snail_step_finished = 0
            count_snail_megastep_finished += 1
            if snail_direction == -1:
                snail_direction = 0
            elif snail_direction == 0:
                snail_direction = 1
            elif snail_direction == 1:
                snail_direction = 2
            elif snail_direction == 2:
                snail_direction = -1
            if count_snail_megastep_finished == 2:
                count_snail_megastep_finished = 0
                count_snail_step += 1
        x += dx
        y += dy
    except IndexError:
        break
data[center_x, center_y] = 255
with tifffile.TiffWriter('prime.tif') as tif:
    tif.write(data)
