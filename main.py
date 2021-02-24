import pygame
pygame.init()

class Brick:
  def __init__(self, xpos, ypos):
    self.xpos = xpos
    self.ypos = ypos
    self.alive = True
  def draw(self):
    if self.alive is True:
      pygame.draw.rect(screen,(255,0,255), (self.xpos, self.ypos, 50, 20))
  def collide(self, x, y):
    if self.alive is True:
      if x+20>self.xpos and x<self.xpos+50 and y+20>self.ypos and y<self.ypos+20:
        self.alive = False
        return True

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Breakout")

doExit = False

clock = pygame.time.Clock()

px = 300
py = 500

bx = 400
by = 450
bVx = 5
bVy = 5

#bricks
b1 = Brick(20,20)
b2 = Brick(200, 20)
b3 = Brick(200, 100)
b4 = Brick(20, 100)
b5 = Brick(20, 180)
b6 = Brick(20, 260)
b7 = Brick(200, 180)
b8 = Brick(200, 260)
b9 = Brick(380, 20)
b10 = Brick(380, 100)
b11 = Brick(380, 180)
b12 = Brick(380, 260)
b13 = Brick(560, 20)
b14 = Brick(560, 100)
b15 = Brick(560, 180)
b16 = Brick(560, 260)
b17 = Brick(740, 20)
b18 = Brick(740, 100)
b19 = Brick(740, 180)
b20 = Brick(740, 260)

while not doExit:

  clock.tick(60)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      doExit = True

  #logic-----------
  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT]:
    px -= 5
  if keys[pygame.K_RIGHT]:
    px += 5
  #physics------
  bx += bVx
  by += bVy

#bounces ball off left and right walls
  if bx < 0 or bx + 20 > 800:
    bVx *= -1

#add code here to bounce off top and bottom walls
  if by < 0 or by + 20 > 600:
    bVy *= -1
#bounces ball off paddle
  #if by + 20 > py and bx  + 20 >  px and bx < px+100:
    #bVy *= -1
  if bx > px and bx <px+200 and by+15 > py:
    bVy *= -1

  if b1.collide(bx, by):
    bVy *= -1
  if b2.collide(bx, by):
    bVy *= -1
  if b3.collide(bx, by):
    bVy *= -1
  if b4.collide(bx, by):
    bVy *= -1
  if b5.collide(bx, by):
    bVy *= -1
  if b6.collide(bx, by):
    bVy *= -1
  if b7.collide(bx, by):
    bVy *= -1
  if b8.collide(bx, by):
    bVy *= -1
  if b9.collide(bx, by):
    bVy *= -1
  if b10.collide(bx, by):
    bVy *= -1
  if b11.collide(bx, by):
    bVy *= -1
  if b12.collide(bx, by):
    bVy *= -1
  if b13.collide(bx, by):
    bVy *= -1
  if b14.collide(bx, by):
    bVy *= -1
  if b15.collide(bx, by):
    bVy *= -1
  if b16.collide(bx, by):
    bVy *= -1
  if b17.collide(bx, by):
    bVy *= -1
  if b18.collide(bx, by):
    bVy *= -1
  if b19.collide(bx, by):
    bVy *= -1
  if b20.collide(bx, by):
    bVy *= -1

  #render--------
  screen.fill((0, 0, 0))

  ###reference for screen size
  #pygame.draw.line(screen, (255, 255, 255), [400, 0], [400, 500], 5)

  pygame.draw.rect(screen, (255, 255, 255), (px, py, 200, 20))

  pygame.draw.circle(screen, (255, 255, 255), (bx, by), 15)

  b1.draw()
  b2.draw()
  b3.draw()
  b4.draw()
  b5.draw()
  b6.draw()
  b7.draw()
  b8.draw()
  b9.draw()
  b10.draw()
  b11.draw()
  b12.draw()
  b13.draw()
  b14.draw()
  b15.draw()
  b16.draw()
  b17.draw()
  b18.draw()
  b19.draw()
  b20.draw()

  pygame.display.flip()

#####
pygame.quit()
