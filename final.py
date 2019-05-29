import pygame
pygame.init()

img = pygame.image.load('yeah3.png')
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("LET'S TRY TO EVOLVE")

font = pygame.font.SysFont('Comic Sans MS', 30)
text = font.render('USE CURSORS, PRESS', 0, (255, 255, 255))
text2 = font.render('RIGHT CONTROL', 0, (255, 255, 255))

class block:

    def __init__(self, lit, x, y):
        self.lit = lit
        self.x = x
        self.y = y

class redsquare:

    def __init__(self, xpos, ypos):
        self.x = xpos
        self.y = ypos

    def mover(self):
        self.x += 10
    def movel(self):
        self.x -= 10
    def moveu(self):
        self.y -= 10
    def moved(self):
        self.y += 10

class posn:

    def __init__(self, x, y):
        self.x = x
        self.y = y

def drawred(x, y):

    pygame.draw.rect(win, (255, 0, 0), (x, y, 10, 10))
    pygame.draw.rect(win, (0, 0, 0), (x+1, y+1, 8, 8))
    pygame.display.update()

def undrawred(x, y):

    pygame.draw.rect(win, (0, 0, 0), (x, y, 10, 10))
    pygame.display.update()

def drawgrid():

    for i in range(0, 500, 10):
        pygame.draw.rect(win, (255, 0, 0), (0, i, 500, 1))
    for i in range(0, 500, 10):
        pygame.draw.rect(win, (255, 0, 0), (i, 0, 1, 500))

    pygame.display.update()

def updatedis(b = []):

    for i in range(0, 2500):
        if b[i].lit == True:
            pygame.draw.rect(win, (255, 255, 255), (b[i].x, b[i].y, 10, 10))
        if b[i].lit == False:
            pygame.draw.rect(win, (0, 0, 0), (b[i].x, b[i].y, 10, 10))

    drawgrid()
    pygame.display.update()

def attr(x, y, b = []):

    for i in range(0, 2500):
        if b[i].x == x and b[i].y == y:
            return i

def posofuns(a = []):

    yeah = []
    nah = []

    for k in range(0, 2500):

        if a[k].x == 0 or a[k].y == 0 or a[k].x == 490 or a[k].y == 490:
            continue

        count = 0

        for i in (a[k].x-10, a[k].x, a[k].x+10):
            for j in (a[k].y-10, a[k].y, a[k].y+10):
                if i == a[k].x and j == a[k].y:
                    continue
                if a[attr(i, j, a)].lit == True:
                    count += 1

        if(count > 3):
            yeah.append(posn(a[k].x, a[k].y))
        else:
            nah.append(posn(a[k].x, a[k].y))

    return yeah, nah

def main():

    k = True
    a = []

    for i in range(0, 500):
        for j in range(0, 500):
            if i%10 == 0 and j%10 == 0:
                a.append(block(False, i, j))

    r = redsquare(0, 0)

    scene0 = True
    scene1 = False
    scene2 = False

    while k:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                k = False

        keys = pygame.key.get_pressed()

        if scene0:

            if keys[pygame.K_RCTRL]:
                scene1 = True
                scene0 = False

            win.blit(img, (0, 0))
            pygame.display.update()

        if scene1:

            updatedis(a)
            if keys[pygame.K_RETURN]:
                scene2 = True
                scene1 = False

            if keys[pygame.K_UP]:
                r.y -= 10
                r.moveu
                undrawred(r.x,r.y+10)
                drawred(r.x, r.y)
                pygame.time.delay(70)
            if keys[pygame.K_DOWN]:
                r.y += 10
                r.moved
                undrawred(r.x,r.y-10)
                drawred(r.x, r.y)
                pygame.time.delay(70)
            if keys[pygame.K_LEFT]:
                r.x -= 10
                r.movel
                undrawred(r.x+10,r.y)
                drawred(r.x, r.y)
                pygame.time.delay(70)
            if keys[pygame.K_RIGHT]:
                r.x += 10
                r.mover
                undrawred(r.x-10,r.y)
                drawred(r.x, r.y)
                pygame.time.delay(70)
            if keys[pygame.K_SPACE]:
                a[attr(r.x, r.y, a)].lit = True
                updatedis(a)

        if scene2:

            count = 0

            for i in range(0, 2500):
                if a[i].lit == False:
                    count += 1

            if count == 2500:
                scene2 = False

            yeah = []
            nah = []

            yeah, nah = posofuns(a)

            for l1 in range(0, len(yeah)):
                a[attr(yeah[l1].x, yeah[l1].y, a)].lit = True
            for l1 in range(0, len(nah)):
                a[attr(nah[l1].x, nah[l1].y, a)].lit = False

            updatedis(a)

main()

pygame.quit()
