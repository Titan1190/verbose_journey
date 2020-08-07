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

'''def create_grid():
    blockSize = 20
    for i in range(0, 24):
        for j in range(0, 24):
            rect = pg.Rect(i*VEL, j*VEL,
            blockSize, blockSize)
            pg.draw.rect(WIN, (255,255,0), rect, 2)
'''
# Include initialization function for head

class Head:

    def __init__(self, x, y):
        self.VEL = 25
        self.SIZE = SIZE
        self.direction = "right"
        self.surface = pg.Rect(x, y, self.SIZE, self.SIZE)
        self.x_pos = []
        self.y_pos = []
        self.color = (88, 214, 141)
        self.last = 0
        self.cooldown = 150

    def move(self,score):
        if self.direction == "up":
            self.surface = self.surface.move(0, -self.VEL)

        if self.direction == "down":
            self.surface = self.surface.move(0, self.VEL)

        if self.direction == "right":
            self.surface = self.surface.move(self.VEL, 0)

        if self.direction == "left":
            self.surface = self.surface.move(-self.VEL, 0)

        self.x_pos.append(self.surface.x)
        self.y_pos.append(self.surface.y)

        if len(self.x_pos) > score + 2:
            self.x_pos.pop(0)
            self.y_pos.pop(0)

    def change_direction(self, event, snake):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w:
                self.direction = "up"
            if event.key == pg.K_s:
                self.direction = "down"
            if event.key == pg.K_d:
                self.direction = "right"
            if event.key == pg.K_a:
                self.direction = "left"

    def draw(self, WIN):
        pg.draw.rect(WIN, self.color, self.surface, 0)

    # For collision of snake so that program knows to end game

    def collide_snake(self, WIN, snake):
        for element in snake[1:]:
            c_point = self.surface.colliderect(element.surface)

            if c_point:
                return True

        return False

    # Delayed reaction due to processing overlay

class Tail:

    def __init__(self, x, y, score):
        self.VEL = 25
        self.SIZE = SIZE
        self.surface = pg.Rect(x, y, self.SIZE, self.SIZE)
        self.color = (130, 224, 170)
        self.score_index = score

    def draw(self, WIN):
        pg.draw.rect(WIN, self.color, self.surface, 0)

    def move(self, snake):
        head = snake[0]
        self.surface = pg.Rect(head.x_pos[self.score_index], head.y_pos[self.score_index], self.SIZE, self.SIZE)
# Need to refrence index of element not yet created however not everytime
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
    #create_grid()
    pg.display.update()

def add_tail(snake, score):
    head = snake[0]
    snake.append(Tail(head.x_pos[score], head.y_pos[score], score))

def leave_screen(body):
    if body.surface.x < 0 or body.surface.x > WIN_WIDTH or body.surface.y < 0 or body.surface.y > WIN_HEIGHT:
        return True

    return False


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
            if isinstance(body, Tail):
                body.move(snake)

            if isinstance(body, Head):
                body.move(score)
                if body.collide_snake(WIN, snake):
                    run = False
                    pg.quit()
                    sys.exit()

                if body.surface.colliderect(apples[0].surface):
                    apples.pop()
                    score +=1
                    apples.append(Apple(snake))
                    add_tail(snake, score)

        if leave_screen(body):
            run = False
            pg.quit()
            sys.exit()

        draw_window(WIN, snake, apples[0])
        clock.tick(6)
        
        for event in pg.event.get():
            if now - last >= head.cooldown:
                last = now
                head.change_direction(event, snake)
            if event.type == pg.QUIT:
                run = False
                pg.quit()
                sys.exit()

main()
