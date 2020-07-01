import pygame
import random
import os
import decimal

pygame.init()

WIN_WIDTH = 800
WIN_HEIGHT = 600


PLAYER = pygame.transform.scale(pygame.image.load(os.path.join('imgs', 'ghost.png')), (80, 120))
HEART = pygame.transform.scale(pygame.image.load(os.path.join('imgs', 'heart.png')), (40, 40))
PROJECTILES = []
PROJECTILES.append(pygame.transform.scale(pygame.image.load(os.path.join('imgs', 'briefcase.png')), (40, 40)))
PROJECTILES.append(pygame.transform.scale(pygame.image.load(os.path.join('imgs', 'tax.png')), (40, 40)))
PROJECTILES.append(pygame.transform.scale(pygame.image.load(os.path.join('imgs', 'graduation.png')), (40, 40)))

WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
STAT_FONT = pygame.font.SysFont("comicsans", 50)

class Player:
    VEL = 15

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.img = PLAYER

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
          self.y += self.VEL
        if keys[pygame.K_w]:
          self.y -= self.VEL
        if keys[pygame.K_d]:
          self.x += self.VEL
        if keys[pygame.K_a]:
          self.x -= self.VEL

    def get_mask(self):
        return pygame.mask.from_surface(self.img)

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))

class Heart:

    def __init__(self):
        self.x = random.randrange(20,WIN_WIDTH - 20)
        self.y = random.randrange(20,WIN_HEIGHT - 20)
        self.img = HEART

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))

    def collide(self, win, player):
        heart_mask = pygame.mask.from_surface(self.img)
        player_mask = player.get_mask()

        offset = (self.x - round(player.x), self.y - round(player.y))
        c_point = player_mask.overlap(heart_mask, offset)

        if c_point:
          return True

        return False

class Projectile:
    def __init__(self):
        axis = random.randrange(0,2) # x or y
        side = random.randrange(0,2) # negative or positive
        x = random.randrange(-40, WIN_WIDTH + 40)
        y = random.randrange(-40, WIN_HEIGHT + 40)

        if axis == 0:
            if side == 0:
                self.x = x
                self.y = -40
            else:
                self.x = x
                self.y = WIN_HEIGHT + 40

        else:
            if side == 0:
                self.x = -40
                self.y = y
            else:
                self.x = WIN_WIDTH + 40
                self.y = y

        self.VEL = random.randrange(8, 12)
        self.delta_x = random.randrange(WIN_WIDTH/4,(WIN_WIDTH*3)/4) - self.x
        self.delta_y = random.randrange(WIN_HEIGHT/4, (WIN_HEIGHT*3)/4) - self.y
        self.img = random.choice(PROJECTILES)

        if self.delta_x < 50:
            self.delta_x += 50



    def move(self):
        if self.delta_x > 0:
            self.x += self.VEL
        else:
            self.x -= self.VEL

        if self.delta_y > 0:
            self.y += abs(float(self.delta_y / self.delta_x)*self.VEL)
        else:
            self.y -= abs(float(self.delta_y / self.delta_x)*self.VEL)

    def collide(self, win, player):
        projectile_mask = pygame.mask.from_surface(self.img)
        player_mask = player.get_mask()

        offset = (round(self.x) - round(player.x), round(self.y) - round(player.y))
        c_point = player_mask.overlap(projectile_mask, offset)

        if c_point:
          return True

        return False

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))

def draw_window(win, heart, player, score, projectiles):
    win.fill((148, 227, 219))
    player.draw(win)
    heart.draw(win)

    for x in projectiles:
        x.draw(win)

    score_label = STAT_FONT.render("Score: " + str(score),1,(255,255,255))
    win.blit(score_label, (WIN_WIDTH - score_label.get_width() - 15, 10))

    pygame.display.update()

def main():
    run = True
    score = 0
    index = 0
    hearts = []
    hearts.append(Heart())
    player = Player(50,50)
    projectiles = []
    projectiles.append(Projectile())

    clock = pygame.time.Clock()


    while run:
        clock.tick(30)
        draw_window(WIN, hearts[0], player, score, projectiles)
        player.move()

        while len(projectiles) <= score / 5:
            projectiles.append(Projectile())

        for projectile in projectiles:
            projectile.move()
            if projectile.collide(WIN, player):
                pygame.quit()
                run = False

            if (projectile.x > WIN_WIDTH + 50) or (projectile.x < -WIN_WIDTH - 50) or (projectile.y > WIN_HEIGHT + 50) or (projectile.y < -WIN_HEIGHT - 50):
                projectiles.pop(index)
            else:
                index+=1

        index = 0

        if hearts[0].collide(WIN, player):
          score+=1
          hearts.pop()
          hearts.append(Heart())

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                run = False

main()
