import time
from random import random

def randomize():
    x = 2*random()
    if x >= 1:
        return True
    else:
        return False

def create_array(x,y):
    arr = [[randomize() for i in range(x)] for j in range(y)]
    return arr


def game_of_life(arr, increments):
    while(increments >= 0):
        count = 0
        past_arr = [row[:] for row in arr]
        for i in range(len(past_arr)):
            for j in range(len(past_arr[i])):
                neighbors = 0
                incr_x = [-1,0,1]
                incr_y = [-1,0,1]

                if (i == 0):
                    incr_y = [-1,0]
                if (i == (len(past_arr[0]) - 1)):
                    incr_y = [0, 1]
                if (j == 0):
                    incr_x = [0,1]
                if (j == (len(past_arr[0]) - 1)):
                    incr_x = [-1,0]

                for x in incr_x:
                    for y in incr_y:
                        if (x != 0 or y != 0) and past_arr[i + x][j + y] == True:
                            neighbors+=1

                print(neighbors)
                count+=1
                if (neighbors == 2 or neighbors == 3) and past_arr[i][j] == True:
                    arr[i][j] == True
                elif neighbors == 3 and past_arr[i][j] == True:
                    arr[i][j] == True
                else:
                    arr[i][j] == False

        print(count)
        print(past_arr)
        time.sleep(1)
        increments -= 1


game_of_life(create_array(10, 10), 1)
