import pygame as pg
import os
import random
import sys

WIN_WIDTH = 600
WIN_HEIGHT = 600
WIN = pg.display.set_mode((WIN_HEIGHT, WIN_HEIGHT))
SIZE = 20
VEL = 25
INITIAL_X = 50
INITIAL_Y = 50


def create_grid():
    blockSize = 20
    for i in range(0, 24):
        for j in range(0, 24):
            rect = pg.Rect(i*VEL, j*VEL,
            blockSize, blockSize)
            pg.draw.rect(WIN, (255,255,0), rect, 2)

# Include initialization function for head

class Head:

    def __init__(self, x, y):
        self.VEL = 25
        self.SIZE = SIZE
        self.direction = "right"
        self.surface = pg.Rect(x, y, self.SIZE, self.SIZE)
        self.dir_list = Direction_List()
        self.color = (88, 214, 141)
        self.last = 0
        self.cooldown = 150

    def move(self):
        if self.direction == "up":
            self.surface = self.surface.move(0, -self.VEL)

        if self.direction == "down":
            self.surface = self.surface.move(0, self.VEL)

        if self.direction == "right":
            self.surface = self.surface.move(self.VEL, 0)

        if self.direction == "left":
            self.surface = self.surface.move(-self.VEL, 0)

        self.dir_list.turn_length += 1
        #print("turn length: {}".format(self.dir_list.turn_length))

    def change_direction(self, event, turns, snake):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w:
                self.direction = "up"
            if event.key == pg.K_s:
                self.direction = "down"
            if event.key == pg.K_d:
                self.direction = "right"
            if event.key == pg.K_a:
                self.direction = "left"

            self.dir_list.length_list.append(self.dir_list.turn_length)
            self.dir_list.turn_length = 0
            self.dir_list.direction_list.append(self.direction)

            self.dir_list.x_pos.append(self.surface.x)
            self.dir_list.y_pos.append(self.surface.y)

            for body in snake[1:]:
                body.dir_list.append(self.direction)

    def draw(self, WIN):
        pg.draw.rect(WIN, self.color, self.surface, 0)

    # For collision of snake so that program knows to end game

    def collide_snake(self, WIN, snake):

        for element in snake[1:]:
            c_point = self.surface.colliderect(element.surface)

            if c_point:
                return True

            return False

class Direction_List:

    def __init__(self):
        self.direction_list = []
        self.x_pos = []
        self.y_pos = []
        self.length_list = []
        self.turn_length = 0

    # Delayed reaction due to processing overlay

class Tail:

    def __init__(self, direction, x, y, score):
        self.VEL = 25
        self.SIZE = SIZE
        self.direction = direction
        self.surface = pg.Rect(x, y, self.SIZE, self.SIZE)
        self.color = (130, 224, 170)
        self.score = score
        self.current = 0
        self.dir_list = []

    def draw(self, WIN):
        pg.draw.rect(WIN, self.color, self.surface, 0)

    def move(self):
        if self.direction == "up":
            self.surface = self.surface.move(0, -self.VEL)

        if self.direction == "down":
            self.surface = self.surface.move(0, self.VEL)

        if self.direction == "right":
            self.surface = self.surface.move(self.VEL, 0)

        if self.direction == "left":
            self.surface = self.surface.move(-self.VEL, 0)

        if len(self.dir_list) != 0:
            self.current += 1


# Need to refrence index of element not yet created however not everytime

    def follow_path(self):
        if len(self.dir_list) != 0:
            if self.current == self.score:
                self.direction = self.dir_list[0]
                self.dir_list.pop(0)
                self.current = 0

class Apple:

    def __init__(self, snake):
        self.VEL = 25
        num_boxes = (WIN_WIDTH - self.VEL) / self.VEL
        overlap = True
        self.x = random.randint(0, num_boxes) * self.VEL
        self.y = random.randint(0, num_boxes) * self.VEL

        while(overlap):
            for body in snake:
                if self.x == body.surface.x or self.y == body.surface.y:
                        self.x = random.randint(0, num_boxes) * self.VEL
                        self.y = random.randint(0, num_boxes) * self.VEL
                        continue
            overlap = False

        self.SIZE = SIZE
        self.color = (231, 76, 60)
        self.surface = pg.Rect(self.x, self.y, self.SIZE, self.SIZE)

    def draw(self, WIN):
        pg.draw.rect(WIN, self.color, self.surface, 0)

def draw_window(win, snake, apple, turns):
    win.fill((0,0,0))
    for body in snake:
        body.draw(win)
    apple.draw(win)
    create_grid()
    pg.display.update()

def add_tail(snake, score):
    head = snake[0]
    tail_score = score
    score = score + 1 # Add Head
    length_list = head.dir_list.length_list[:]
    length_list.append(head.dir_list.turn_length) # Add distance currently traveled

    list_index = len(length_list) - 1 #reverse index

    while(list_index >= 0):
        score -= length_list[list_index]
        if score <= 0:
            score = abs(score)
            if list_index == 0:
                dir = 'right'
            else:
                dir = head.dir_list.direction_list[list_index - 1]

            if dir == "up":
                x_pos = head.dir_list.x_pos[list_index - 1]
                y_pos = head.dir_list.y_pos[list_index - 1] - VEL * score

            if dir == "down":
                x_pos = head.dir_list.x_pos[list_index - 1]
                y_pos = head.dir_list.y_pos[list_index - 1] + VEL * score

            if dir == "left":
                x_pos = head.dir_list.x_pos[list_index - 1] - VEL * score
                y_pos = head.dir_list.y_pos[list_index - 1]

            if dir == "right":

                if list_index == 0:
                    x_pos = INITIAL_X + VEL * score
                    y_pos = head.dir_list.y_pos[list_index - 1]
                else:
                    x_pos = head.dir_list.x_pos[list_index - 1] + VEL * score
                    y_pos = head.dir_list.y_pos[list_index - 1]

            snake.append(Tail(dir, x_pos, y_pos, tail_score))
            break

        list_index -= 1

def main():
    run = True
    head = Head(INITIAL_X, INITIAL_Y)
    clock = pg.time.Clock()
    snake = [head]
    apples = []
    apples.append(Apple(snake))
    turns = []
    score = 0
    now = 0
    last = 0

    while run:
        now = pg.time.get_ticks()
        for body in snake:
            body.move()

            if isinstance(body, Tail):
                body.follow_path()
                print(' ,'.join(body.dir_list))
                #print(body)
                print("Score: {}, Current: {}".format(body.score, body.current))


            if isinstance(body, Head):
                if body.collide_snake(WIN, snake):
                    run = False
                    pg.quit()
                    sys.exit()

                if body.surface.colliderect(apples[0].surface):
                    apples.pop()
                    score +=1
                    apples.append(Apple(snake))
                    add_tail(snake, score)


        draw_window(WIN, snake, apples[0], turns)
        clock.tick(6)

        for event in pg.event.get():
            if now - last >= head.cooldown:
                last = now
                head.change_direction(event, turns, snake)
            if event.type == pg.QUIT:
                run = False
                '''print("Direction List: {}".format(head.dir_list.direction_list))
                print("X_Pos: {}".format(head.dir_list.x_pos))
                print("Y_Pos: {}".format(head.dir_list.y_pos))
                print("Current Length List: {}".format(head.dir_list.length_list))
                print("Current Length: {}".format(head.dir_list.turn_length))
                '''
                pg.quit()
                sys.exit()

main()
