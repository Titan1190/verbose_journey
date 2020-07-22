import pygame as pg
import os
import random
import sys

WIN_WIDTH = 600
WIN_HEIGHT = 600
WIN = pg.display.set_mode((WIN_HEIGHT, WIN_HEIGHT), )
SIZE = 20
VEL = 25
INITIAL_X = 50
INITIAL_Y = 50


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
        self.cooldown = 200

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


    def change_direction(self, event):
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


class Tail:

    def __init__(self, direction, x, y, dir_index):
        self.VEL = 25
        self.SIZE = SIZE
        self.direction = direction
        self.surface = pg.Rect(x, y, self.SIZE, self.SIZE)
        self.color = (130, 224, 170)
        self.dir_index = dir_index

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

    def follow_path(self, snake):
        head = snake[0]
        if self.direction != head.direction:
            if self.surface.x == head.dir_list.x_pos[self.dir_index] or self.surface.y == head.dir_list.y_pos[self.dir_index]:
                self.dir_index += 1
                self.direction = head.dir_list.direction_list[self.dir_index]

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


def draw_window(win, snake, apple):
    win.fill((0,0,0))
    for body in snake:
        body.draw(win)
    apple.draw(win)
    pg.display.update()

def add_tail(snake, score):
    head = snake[0]
    score = score + 1 # Add Head
    length_list = head.dir_list.length_list[:]
    length_list.append(head.dir_list.turn_length) # Add distance currently traveled

    list_index = len(length_list) - 1 #reverse index
    while(list_index >= 0):
        score -= length_list[list_index]
        if score <= 0:
            score = abs(score)
            print("Score {}". format(score))
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
                x_pos = head.dir_list.x_pos[list_index - 1] + VEL * score
                y_pos = head.dir_list.y_pos[list_index - 1]

            if dir == "right":
                if list_index == 0:
                    x_pos = INITIAL_X - VEL * score
                    y_pos = head.dir_list.y_pos[list_index - 1]
                else:
                    x_pos = head.dir_list.x_pos[list_index - 1] - VEL * score
                    y_pos = head.dir_list.y_pos[list_index - 1]

            snake.append(Tail(dir, x_pos, y_pos, list_index - 1))
            break
        list_index -= 1

def main():
    run = True
    head = Head(INITIAL_X, INITIAL_Y)
    clock = pg.time.Clock()
    snake = [head]
    apples = []
    apples.append(Apple(snake))
    score = 0
    now = 0
    last = 0

    while run:
        now = pg.time.get_ticks()
        for body in snake:
            body.move()

            if isinstance(body, Tail):
                body.follow_path(snake)

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


        draw_window(WIN, snake, apples[0])
        clock.tick(6)

        for event in pg.event.get():
            if now - last >= head.cooldown:
                last = now
                head.change_direction(event)
            if event.type == pg.QUIT:
                print(head.dir_list.direction_list)
                print(head.dir_list.x_pos)
                print(head.dir_list.y_pos)
                print(head.dir_list.length_list)
                run = False
                pg.quit()
                sys.exit()

main()
