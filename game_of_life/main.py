import time
from random import random

import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np

# Randomize elements in array
def randomize():
    x = 2*random()
    if x >= 1:
        return 1
    else:
        return 0

# Iniatialize Array with randomized elements
def create_array(x,y):
    arr = [[randomize() for i in range(x)] for j in range(y)]
    return arr

# Implements game of life
def game_of_life(arr, increments):
    cmap = colors.ListedColormap(['cyan', '#85F077'])
    bounds = [0,1,2]
    norm = colors.BoundaryNorm(bounds, cmap.N)

    while(increments >= 0):
        count = 0
        past_arr = [row[:] for row in arr]

        for i in range(len(past_arr)):
            for j in range(len(past_arr[i])):
                neighbors = 0
                incr_x = [-1,0,1]
                incr_y = [-1,0,1]

                if (i == 0):
                    incr_y = [1,0]
                if (i == (len(past_arr[i]) - 1)):
                    incr_y = [0, -1]
                if (j == 0):
                    incr_x = [0,1]
                if (j == (len(past_arr[i]) - 1)):
                    incr_x = [-1,0]

                for x in incr_x:
                    for y in incr_y:
                        if (x != 0 or y != 0) and past_arr[i + y][j + x] == 1:
                            neighbors+=1

                if (neighbors == 2 or neighbors == 3) and past_arr[i][j] == 1:
                    arr[i][j] == 1
                elif neighbors == 3 and past_arr[i][j] == 0:
                    arr[i][j] == 1
                else:
                    arr[i][j] == 0

        fig, ax = plt.subplots()
        ax.imshow(arr, cmap=cmap, norm=norm)
        plt.show()
        time.sleep(1)
        increments -= 1


game_of_life(create_array(10, 10), 3)
