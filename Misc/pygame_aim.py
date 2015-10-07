import pygame
import math

asurf = pygame.image.load('down_arrow.png')
asurf = pygame.transform.scale(asurf, (30, 50))

class Aimer(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = asurf
        self.rect = self.image.get_rect()
        
    def rotate_with_mouse(self, ball_x, ball_y):
        pos = pygame.mouse.get_pos()
        angle = 360-math.atan2(pos[1]-450,pos[0]-50)*180/math.pi
        rotimage = pygame.transform.rotate(self.image, angle)
        # TODO Place centre on ball, not centre of image
        rect = rotimage.get_rect(center=(ball_x, ball_y))
        screen.blit(rotimage,rect) 

    def setposition(self, x_coord, y_coord):
        self.rect.x = x_coord
        self.rect.y = y_coord

pygame.init()
window = pygame.display.set_mode((500,500))
screen = pygame.display.get_surface()

ball = Aimer()
ball.setposition(50, 450)

finished = True
while finished:
    screen.fill((0,0,0))
    
    ball.rotate_with_mouse(50, 450)
    pygame.display.update()
    pygame.event.get()
