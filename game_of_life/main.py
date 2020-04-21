import time




def game_of_life(arr):
    incr = [-1,0,1]
    neighbors = 0
    past_arr = [row[:] for row in arr]

    for i in past_arr:
        for j in past_arr[i]:
            
            for x in incr:
                for y in incr:

                    if x != 0 or y != 0 and past_arr[i + x][j + y] == True:
                        neighbors+=1

            if (neighbors == 2 or neighbors == 3) and past_arr[i][j] == True:
                arr[i][j] == True
            elif neighbors == 3 and past_arr[i][j] = True:
                arr[i][j] == True
            else:
                arr[i][j] == False
