import time
from random import random

import pygame


DEAD_COLOR = (90, 90, 90)
WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400
SLEEP_TIME = .05
arr_length = 40

def light_rainbow():
    arr =[140 + int(random()*115) for x in range(3)]
    return arr

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
def create_grid(arr, LIVE_COLOR):
    blockSize = WINDOW_WIDTH / len(arr)
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            rect = pygame.Rect(i*blockSize, j*blockSize,
            blockSize, blockSize)
            if arr[i][j] == 0:
                pygame.draw.rect(SCREEN, DEAD_COLOR, rect, 0)
            else:
                pygame.draw.rect(SCREEN, LIVE_COLOR, rect, 0)

def game_of_life(arr):
        past_arr = [x[:] for x in arr]

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
                    arr[i][j] = 1
                elif (neighbors == 3 and past_arr[i][j] == 0):
                    arr[i][j] = 1
                else:
                    arr[i][j] = 0
        return arr

def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(DEAD_COLOR)
    arr = create_array(arr_length,arr_length)

    while True:
        color_arr = light_rainbow()
        LIVE_COLOR = (color_arr[0], color_arr[1], color_arr[2])

        for x in range(50):
            create_grid(arr, LIVE_COLOR)
            for y in range(len(color_arr)):
                    color_arr[y] -= 1
            LIVE_COLOR = (color_arr[0], color_arr[1], color_arr[2])
            time.sleep(SLEEP_TIME / 75)
            pygame.display.update()

        arr = game_of_life(arr)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


main()
