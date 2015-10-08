import pygame, math, sys, time
from pygame.locals import *

'''
CLASSES
'''

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([5, 5])
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()

    def setposition(self, x_coord, y_coord):
        self.rect.x = x_coord
        self.rect.y = y_coord



class World():
    '''This will hold the platforms and the goal. 
    nb. In this game, the world moves left and right rather than the player'''
    def __init__(self, level, block_size, colour_platform, colour_goals):
        self.platforms = []
        self.goals = []
        self.posn_y = 0
        self.colour = colour_platform
        self.colour_goals = colour_goals
        self.block_size = block_size
        
        for line in level:
            self.posn_x = 0
            for block in line:
                if block == "-":
                    self.platforms.append(pygame.Rect(self.posn_x, self.posn_y, block_size, block_size))
                if block == "G":
                    self.goals.append(pygame.Rect(self.posn_x, self.posn_y, block_size, block_size))
                self.posn_x = self.posn_x + block_size
            self.posn_y = self.posn_y + block_size
    # Unused       
    def move(self, dist):
        '''move the world dist pixels right (a negative dist means left)'''
        for block in self.platforms + self.goals:
            block.move_ip(dist,0)
    # Unused
    def collided_get_y(self, player_rect):
        '''get the y value of the platform the player is currently on'''
        return_y = -1
        for block in self.platforms:
            if block.colliderect(player_rect):
                return_y = block.y - block.height + 1
        return return_y
    # Unused    
    def at_goal(self, player_rect):
        '''return true if the player is currently in contact with the goal. False otherwise'''
        for block in self.goals:
            if block.colliderect(player_rect):
                return True
        return False
    # Unused
    def update(self, screen):
        '''draw all the rectangles onto the screen'''
        for block in self.platforms:
            pygame.draw.rect(screen, self.colour, block, 0)
        for block in self.goals:
            pygame.draw.rect(screen, self.colour_goals, block, 0)

    def ball_collided(self, ball_rect):
        '''check has the ball hit the platform'''
        return_y = False
        for block in self.platforms:
            if block.colliderect(ball_rect):
                return_y = True
        return return_y

class Aimer(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = asurf
        self.rect = self.image.get_rect()
        
    def rotate_with_mouse(self, ball_x, ball_y):
        pos = pygame.mouse.get_pos()
        angle = 360-math.atan2(pos[1]-ball_y,pos[0]-ball_x)*180/math.pi
        rotimage = pygame.transform.rotate(self.image, angle)
        # TODO Place centre on ball, not centre of image
        rect = rotimage.get_rect(center=(ball_x, ball_y))
        screen.blit(rotimage,rect) 

    def setposition(self, x_coord, y_coord):
        self.rect.x = x_coord
        self.rect.y = y_coord


'''
END CLASSES
'''


# Util Methods

# Unused
def getmaxdistance(power, angle_radians):
    a = math.pow (power, 2)
    b = math.sin(2 * angle_radians)
    c = accel_gravity
    
    return (a * b) / c

def getmaxdistance_variableheight(power, angle_radians):
    a = power * math.cos(angle_radians)
    b = power * math.sin(angle_radians)
    c = 2 * accel_gravity * start_height

    return (a / accel_gravity) * (b + math.sqrt(math.pow(b, 2) + c))


def getposition(x_coord, angle_radians, power):
    a = x_coord * math.tan(angle_radians)
    b = accel_gravity * math.pow(x_coord, 2)
    c = 2 * math.pow(power * math.cos(angle_radians), 2)
    
    return start_height + a - (b / c)
    

# OPTIONS
level=[
	"                              ",
	"                              ",
	"                              ",
	"                              ",
	"                              ",
	"                              ",
        "                              ",
        "                              ",
        "                              ",
        "                              ",
        "                              ",
        "                              ",
        "                              ",
        "                              ",
        "                              ",
	"                              ",
	"-----------------------------G"]
platform_colour = (100,100,100)
goal_colour = (0,0,255)
asurf = pygame.image.load('../docs/images/down_arrow.png')
asurf = pygame.transform.scale(asurf, (30, 50))


# Init game
pygame.init()
screen_size_x = 1000
screen_size_y = 500

window = pygame.display.set_mode((screen_size_x,screen_size_y))
screen = pygame.display.get_surface()

# Init distances
offset_x = 50
offset_y = 450
power = 70
angle = 80
intervals = 200
accel_gravity = 9.807
angle_radians = math.radians(angle)
start_height = 0

max_distance = getmaxdistance_variableheight(power, angle_radians)
x_interval = max_distance / intervals

# Init obects
clock = pygame.time.Clock()
ball = Ball()
ball_plain = pygame.sprite.RenderPlain(ball)
world = World(level, 30, platform_colour,goal_colour )

arrow = Aimer()
arrow.setposition(offset_x, offset_y)

aiming_mode = True
interval_multiplier = 1

# GAME LOOP
while True:
    # Init loop vars
    screen.fill((0,0,0))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            start = time.perf_counter()

        if aiming_mode: 
            if event.type == pygame.MOUSEBUTTONUP:
                # Setting power based on time
                end = time.perf_counter()
                elapsed = end - start
                power = elapsed * 200
 
                #using absolute value to set angle of aimer
                pos = pygame.mouse.get_pos()
                angle = math.fabs(math.atan2(pos[1]-offset_y,pos[0]-offset_x)*180/math.pi)
                angle_radians = math.radians(angle)

                # Stopping aiming arrow from showing
                aiming_mode = False

                # Resetting values for new shot
                interval_multiplier = 1

    # Set aimer position
    if aiming_mode:
        arrow.rotate_with_mouse(offset_x, offset_y)

    # Set ball position
    if not aiming_mode:
        current_x = interval_multiplier * x_interval
        current_y = offset_y - getposition(current_x, angle_radians, power)

        ball.setposition(current_x, current_y)
        ball_plain.draw(screen)
        
        aiming_mode = world.ball_collided(ball.rect)
        interval_multiplier = interval_multiplier + 1
        
    world.update(screen)
    pygame.display.update()

