import turtle
import math

# 
power = 50
angle = 80
start_height = 50
min_y_coord = -70

# Constants
intervals = 50
accel_gravity = 9.807
angle_radians = math.radians(angle)

# ledge
ledge_start = 60
ledge_end = 120
ledge_height = 20


# create ledge to land on
ledge = turtle.Turtle()
ledge.hideturtle()
ledge.penup()
ledge.setposition(ledge_start,ledge_height)
ledge.pendown()
ledge.setposition(ledge_end,ledge_height)


screen = turtle.Screen()
golf_ball = turtle.Turtle()
golf_ball.hideturtle()
golf_ball.penup()
golf_ball.setposition(0,start_height)
#golf_ball = turtle.setposition(0,start_height)
golf_ball.pendown()





def getposition(x_coord, angle_radians, power):
    a = x_coord * math.tan(angle_radians)
    b = accel_gravity * math.pow(x_coord, 2)
    c = 2 * math.pow(power * math.cos(angle_radians), 2)
    '''
    print ("abc")
    print (a)
    print (b)
    print (c)
    '''
    
    return start_height + a - (b / c)
    

def getmaxdistance(power, angle_radians):
    a = math.pow (power, 2)
    b = math.sin(2 * angle_radians)
    c = accel_gravity
    
    return (a * b) / c

# Not working
def getmaxdistance_variableheight(power, angle_radians):
    a = power * math.cos(angle_radians)
    b = power * math.sin(angle_radians)
    c = 2 * accel_gravity * start_height

    return (a / accel_gravity) * (b + math.sqrt(math.pow(b, 2) + c))

def check_collision (x_coord, y_coord):
    if (ledge_start < x_coord < ledge_end):
        if (ledge_height + 5 > y_coord > ledge_height - 5):
            print ("setting col 1")
            return True
    elif (y_coord < min_y_coord):
        print ("setting col 2")
        return True
        
    return False


# get max distance
max_distance = getmaxdistance_variableheight(power, angle_radians)
print("max_distance")
print(max_distance)

# get the interval on the y axis
x_interval = max_distance / intervals

'''
for i in range(1 , intervals + 1):
    current_x = i * x_interval
    current_y = getposition(current_x, angle_radians, power)
    
    print("x and y for: " + str(i))
    print (current_x)
    print (current_y)

    golf_ball = turtle.setposition(current_x, current_y)
'''
current_y =  start_height
i = 1
collision = False
while not collision:
    current_x = i * x_interval
    current_y = getposition(current_x, angle_radians, power)
    
    print("x and y for: " + str(i))
    print (current_x)
    print (current_y)

    golf_ball.setposition(current_x, current_y)
    i = i + 1

    collision = check_collision(current_x, current_y)

    
