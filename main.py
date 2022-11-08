import pygame
import random
import math


# Initialize the pygame
pygame.init()


def swap(x_src, y_src, x_dest, y_dest):
    if y_src < y_dest:
        y_src, y_dest = y_dest, y_src
        x_src, x_dest = x_dest, x_src
    return x_src, y_src, x_dest, y_dest


def slope(x1, y1, x2, y2):
    return (y2 - y1)/(x2 - x1)


def intercept(x, y, m):
    return y - m*x

def checkcondition(x1, y1):
    c1 = y1 < team_red_1Y + 32
    c2 = y1 > team_red_1Y - 32
    c3 = x1 < team_red_1X + 32
    c4 = x1 > team_red_1X - 32
    c5 = y1 < team_red_2Y + 32
    c6 = y1 > team_red_2Y - 32
    c7 = x1 < team_red_2X + 32
    c8 = x1 > team_red_2X - 32
    c9 = y1 < team_red_3Y + 32
    c10 = y1 > team_red_3Y - 32
    c11 = x1 < team_red_3X + 32
    c12 = x1 > team_red_3X - 32
    return c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12


def playerObstacle(x1, y1, x2, y2):
    x1, y1, x2, y2 = swap(x1, y1, x2, y2)
    if(x1-x2 != 0 and y1-y2 !=0):
        m_test = slope(x1, y1, x2, y2)
        c_test = intercept(x2, y2, m_test)

        while(y1 >= y2):
            #print(0)
            y1 = y1 - 0.1
            x1 = (y1 - c_test) / m_test
            c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12 = checkcondition(x1, y1)


            if c1 and c2 and c3 and c4:
                return True
            if c5 and c6 and c7 and c8:
                return True
            if c9 and c10 and c11 and c12:
                return True
        return False
    else:
        while (y1 >= y2):
            # print(0)
            y1 = y1 - 0.1
            c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12 = checkcondition(x1, y1)

            if c1 and c2 and c3 and c4:
                return True
            if c5 and c6 and c7 and c8:
                return True
            if c9 and c10 and c11 and c12:
                return True
        return False


def ballMovement(ball_coordinate_x, ball_coordinate_y, m_ball, c_ball):
    ball_coordinate_y = ball_coordinate_y - 1
    if m_ball == 5000:
        return ball_coordinate_x,ball_coordinate_y
    return (ball_coordinate_y-c_ball)/m_ball, ball_coordinate_y


def cost_calculation(a, b, c, d):
	cost = math.sqrt((a-b) * (a-b) + (c-d) * (c-d)) + math.sqrt((a-288) * (a-288) + (c-0) * (c-0))
	return cost


def cost_calculation2(a, b, c, d, e, f):
	cost = math.sqrt((a-b) * (a-b) + (c-d) * (c-d)) + math.sqrt((a-e) * (a-e) + (c-f) * (c-f)) + math.sqrt((e-288) * (e-288) + (f-0) * (f-0))
	return cost


def cost_calculation3(a, b, c, d, e, f, g, h):
    cost = math.sqrt((a-b) * (a-b) + (c-d) * (c-d)) + math.sqrt((a-e) * (a-e) + (c-f) * (c-f)) + math.sqrt((g-e) * (g-e) + (h-f) * (h-f)) + math.sqrt((g-288) * (g-288) + (h-0) * (h-0))
    return cost

# create the screen
screen = pygame.display.set_mode((576,768))
background = pygame.image.load('Field.png')

# Title and Icon
icon = pygame.image.load('logo.png')
pygame.display.set_icon(icon)


# Setting the ball
ball = pygame.image.load('ball.png')
ball_coordinate_x, ball_coordinate_y = 288-16, 384-16

# Setting Environment Location
blue_center_kicker = pygame.image.load('TeamBlue.png')
blue_center_kickerX, blue_center_kickerY = 288, 384

team_blue_1 = pygame.image.load('TeamBlue.png')
team_blue_1X, team_blue_1Y= random.randint(3,14)*32, random.randint(1,5)*32

team_blue_2 = pygame.image.load('TeamBlue.png')
team_blue_2X, team_blue_2Y = random.randint(1,16)*32, random.randint(6,10)*32

team_blue_3 = pygame.image.load('TeamBlue.png')
team_blue_3X, team_blue_3Y = random.randint(1,16)*32, random.randint(6,10)*32

team_red_1 = pygame.image.load('TeamRed.png')
team_red_1X,team_red_1Y = random.randint(3,14)*32, random.randint(1,5)*32

team_red_2 = pygame.image.load('TeamRed.png')
team_red_2X, team_red_2Y = random.randint(1,16)*32, random.randint(6,10)*32

team_red_3 = pygame.image.load('TeamRed.png')
team_red_3X, team_red_3Y = random.randint(1,16)*32, random.randint(6,10)*32

goaly=0
goalx=288

Array_cost=[]
Array_cost.append(cost_calculation(team_blue_1X,blue_center_kickerX,team_blue_1Y,blue_center_kickerY))
Array_cost.append(cost_calculation(team_blue_2X,blue_center_kickerX,team_blue_2Y,blue_center_kickerY))
Array_cost.append(cost_calculation(team_blue_3X,blue_center_kickerX,team_blue_3Y,blue_center_kickerY))

Array_cost.append(cost_calculation2(team_blue_1X,blue_center_kickerX,team_blue_1Y,blue_center_kickerY,team_blue_2X,team_blue_2Y))
Array_cost.append(cost_calculation2(team_blue_1X,blue_center_kickerX,team_blue_1Y,blue_center_kickerY,team_blue_3X,team_blue_3Y))
Array_cost.append(cost_calculation2(team_blue_2X,blue_center_kickerX,team_blue_2Y,blue_center_kickerY,team_blue_3X,team_blue_3Y))
Array_cost.append(cost_calculation2(team_blue_2X,blue_center_kickerX,team_blue_2Y,blue_center_kickerY,team_blue_1X,team_blue_1Y))
Array_cost.append(cost_calculation2(team_blue_3X,blue_center_kickerX,team_blue_3Y,blue_center_kickerY,team_blue_3X,team_blue_2Y))
Array_cost.append(cost_calculation2(team_blue_3X,blue_center_kickerX,team_blue_3Y,blue_center_kickerY,team_blue_1X,team_blue_1Y))

Array_cost.append(cost_calculation3(team_blue_1X,blue_center_kickerX,team_blue_1Y,blue_center_kickerY,team_blue_2X,team_blue_2Y,team_blue_3X,team_blue_3Y))
Array_cost.append(cost_calculation3(team_blue_1X,blue_center_kickerX,team_blue_1Y,blue_center_kickerY,team_blue_3X,team_blue_3Y,team_blue_2X,team_blue_2Y))
Array_cost.append(cost_calculation3(team_blue_2X,blue_center_kickerX,team_blue_2Y,blue_center_kickerY,team_blue_3X,team_blue_3Y,team_blue_1X,team_blue_1Y))
Array_cost.append(cost_calculation3(team_blue_2X,blue_center_kickerX,team_blue_2Y,blue_center_kickerY,team_blue_1X,team_blue_1Y,team_blue_3X,team_blue_3Y))
Array_cost.append(cost_calculation3(team_blue_3X,blue_center_kickerX,team_blue_3Y,blue_center_kickerY,team_blue_2X,team_blue_2Y,team_blue_1X,team_blue_1Y))
Array_cost.append(cost_calculation3(team_blue_3X,blue_center_kickerX,team_blue_3Y,blue_center_kickerY,team_blue_1X,team_blue_1Y,team_blue_2X,team_blue_2Y))

test_c_x_y = playerObstacle(blue_center_kickerX, blue_center_kickerY, team_blue_1X, team_blue_1Y)
check_1x_1y = playerObstacle(goalx, goaly, team_blue_1X, team_blue_1Y)
check_2x_2y = playerObstacle(blue_center_kickerX, blue_center_kickerY, team_blue_2X, team_blue_2Y)
test_2x_2y = playerObstacle(goalx, goaly, team_blue_2X, team_blue_2Y)
check_3x_3y = playerObstacle(blue_center_kickerX, blue_center_kickerY, team_blue_3X, team_blue_3Y)
test_3x_3y = playerObstacle(goalx, goaly, team_blue_3X, team_blue_3Y)
check_1x_1y_2x_2y = playerObstacle(team_blue_1X, team_blue_1Y, team_blue_2X, team_blue_2Y)
check_1x_3y = playerObstacle(team_blue_1X, team_blue_1Y, team_blue_3X, team_blue_3Y)
check_2x_2y_3x_3y = playerObstacle(team_blue_2X, team_blue_2Y, team_blue_3X, team_blue_3Y)



if( test_c_x_y or check_1x_1y):
    Array_cost[0] = 50000
if(check_2x_2y or test_2x_2y):
    Array_cost[1] = 50000
if(check_3x_3y or test_3x_3y):
    Array_cost[2] = 50000
if(test_c_x_y or check_1x_1y_2x_2y or test_2x_2y):
    Array_cost[3] = 50000
if(test_c_x_y or check_1x_3y or test_3x_3y):
    Array_cost[4] = 50000
if(check_2x_2y or check_2x_2y_3x_3y or test_3x_3y):
    Array_cost[5] = 50000
if(check_2x_2y or check_1x_1y_2x_2y or check_1x_1y):
    Array_cost[6] = 50000
if(check_3x_3y or check_2x_2y_3x_3y or test_2x_2y):
    Array_cost[7] = 50000
if(check_3x_3y or check_1x_3y or check_1x_1y):
    Array_cost[8] = 50000
if(test_c_x_y or check_1x_1y_2x_2y or check_2x_2y_3x_3y or test_3x_3y):
    Array_cost[9] = 50000
if(test_c_x_y or check_1x_3y or check_2x_2y_3x_3y or test_2x_2y):
    Array_cost[10] = 50000
if(check_2x_2y or check_2x_2y_3x_3y or check_1x_3y or check_1x_1y):
    Array_cost[11] = 50000
if(check_2x_2y or check_1x_1y_2x_2y or check_1x_3y or test_3x_3y):
    Array_cost[12] = 50000
if(check_3x_3y or check_2x_2y_3x_3y or check_1x_1y_2x_2y or check_1x_1y):
    Array_cost[13] = 50000
if(check_3x_3y or check_1x_3y or check_1x_1y_2x_2y or test_2x_2y):
    Array_cost[14] = 50000


Array_index = []
for i in range (1,16):
    Array_index.append(i)

for i in range(1, len(Array_cost)):

    key = Array_cost[i]
    key2 = Array_index[i]
    j = i - 1
    while j >= 0 and key < Array_cost[j]:
        Array_cost[j + 1] = Array_cost[j]
        Array_index[j + 1] = Array_index[j]
        j -= 1
    Array_cost[j + 1] = key
    Array_index[j + 1] = key2


print(Array_cost)
print(Array_index)

slope_1 = slope(team_blue_1X, team_blue_1Y, blue_center_kickerX, blue_center_kickerY) if (blue_center_kickerX - team_blue_1X) != 0 else 50000
slope_2 = slope(blue_center_kickerX, blue_center_kickerY, team_blue_2X, team_blue_2Y) if (blue_center_kickerX - team_blue_2X) != 0 else 50000
slope_3 = slope(blue_center_kickerX, blue_center_kickerY, team_blue_3X, team_blue_3Y) if (blue_center_kickerX - team_blue_3X) != 0 else 50000
slope_4 = slope(team_blue_1X, team_blue_1Y, goalx, goaly) if (team_blue_1X - goalx) != 0 else 50000
slope_5 = slope(team_blue_2X, team_blue_2Y, goalx, goaly) if (team_blue_2X - goalx) != 0 else 50000
slope_6 = slope(team_blue_3X, team_blue_3Y, goalx, goaly) if (team_blue_3X - goalx) != 0 else 50000
slope_7 = slope(team_blue_1X, team_blue_1Y, team_blue_2X, team_blue_2Y) if (team_blue_1X - team_blue_2X) != 0 else 50000
slope_8 = slope(team_blue_1X, team_blue_1Y, team_blue_3X, team_blue_3Y) if (team_blue_1X - team_blue_3X) != 0 else 50000
slope_9 = slope(team_blue_3X, team_blue_3Y, team_blue_2X, team_blue_2Y) if (team_blue_2X - team_blue_3X) != 0 else 50000

intercept_1 = intercept(blue_center_kickerX, blue_center_kickerX, slope_1)
intercept_2 = intercept(blue_center_kickerX, blue_center_kickerY, slope_2)
intercept_3 = intercept(blue_center_kickerX, blue_center_kickerY, slope_3)
intercept_4 = intercept(goalx, goaly, slope_4)
intercept_5 = intercept(goalx, goaly, slope_5)
intercept_6 = intercept(goalx, goaly, slope_6)

intercept_7 = intercept(team_blue_1X, team_blue_1Y, slope_7)
intercept_8 = intercept(team_blue_1X, team_blue_1Y, slope_8)
intercept_9 = intercept(team_blue_3X, team_blue_3Y, slope_9)

#Setting the Cost

cost = pygame.font.Font('freesansbold.ttf', 18).render("Optimal Cost: "+str(round(Array_cost[0],2)), True, (255, 255, 255), (0, 0, 0))
costRect = cost.get_rect()
costRect.center = (288,700)


cost4 = pygame.font.Font('freesansbold.ttf', 18).render(" Secondary Cost: "+str(round(Array_cost[1],2)), True, (255, 255, 255), (0, 0, 0))
costRect4 = cost4.get_rect()
costRect4.center = (288,720)

# GameOver cost

cost2 = pygame.font.Font('freesansbold.ttf', 18).render("Can't Score, Game Over", True, (255, 255, 255), (0, 0, 0))
costRect2 = cost2.get_rect()
costRect2.center = (288, 576)

# GameOver cost

cost3 = pygame.font.Font('freesansbold.ttf', 18).render("Goal!", True, (255, 255, 255), (0, 0, 0))
costRect3 = cost3.get_rect()
costRect3.center = (288, 576)

#game loop
running = True
while running:
    # RGB background
    screen.fill((0, 128, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(cost, costRect)
    screen.blit(cost4, costRect4)
    screen.blit(blue_center_kicker, (blue_center_kickerX, blue_center_kickerY))
    screen.blit(team_blue_1, (team_blue_1X, team_blue_1Y))
    screen.blit(team_blue_2, (team_blue_2X, team_blue_2Y))
    screen.blit(team_blue_3, (team_blue_3X, team_blue_3Y))
    screen.blit(team_red_1, (team_red_1X, team_red_1Y))
    screen.blit(team_red_2, (team_red_2X, team_red_2Y))
    screen.blit(team_red_3, (team_red_3X, team_red_3Y))


    # #MOVING THE BALL
    screen.blit(ball, (ball_coordinate_x, ball_coordinate_y))

    if Array_cost[0] == 50000:
        screen.blit(cost2, costRect2)
    else:
        if Array_index[0] == 1:
            if ball_coordinate_y > team_blue_1Y:
                ball_coordinate_x, ball_coordinate_y = ballMovement(ball_coordinate_x, ball_coordinate_y, slope_1, intercept_1)
            elif ball_coordinate_y > 0:
                ball_coordinate_x, ball_coordinate_y = ballMovement(ball_coordinate_x, ball_coordinate_y, slope_4, intercept_4)

        if Array_index[0] == 2:
            if ball_coordinate_y > team_blue_2Y:
                ball_coordinate_x, ball_coordinate_y = ballMovement(ball_coordinate_x, ball_coordinate_y, slope_2, intercept_2)
            elif ball_coordinate_y > 0:
                ball_coordinate_x, ball_coordinate_y = ballMovement(ball_coordinate_x, ball_coordinate_y, slope_5, intercept_5)

        if Array_index[0] == 3:
            if ball_coordinate_y > team_blue_3Y:
                ball_coordinate_x, ball_coordinate_y = ballMovement(ball_coordinate_x, ball_coordinate_y, slope_3, intercept_3)
            elif ball_coordinate_y > 0:
                ball_coordinate_x, ball_coordinate_y = ballMovement(ball_coordinate_x, ball_coordinate_y, slope_6, intercept_6)

        if Array_index[0] == 4:
            if ball_coordinate_y > team_blue_1Y:
                ball_coordinate_x, ball_coordinate_y = ballMovement(ball_coordinate_x, ball_coordinate_y, slope_1, intercept_1)
            elif ball_coordinate_y > team_blue_2Y:
                ball_coordinate_x, ball_coordinate_y = ballMovement(ball_coordinate_x, ball_coordinate_y, slope_7, intercept_7)
            elif ball_coordinate_y > 0:
                ball_coordinate_x, ball_coordinate_y = ballMovement(ball_coordinate_x, ball_coordinate_y, slope_5, intercept_5)

        if Array_index[0] == 5:
            if ball_coordinate_y > team_blue_1Y:
                ball_coordinate_x, ball_coordinate_y = ballMovement(ball_coordinate_x, ball_coordinate_y, slope_1, intercept_1)
            elif ball_coordinate_y > team_blue_3Y:
                ball_coordinate_x, ball_coordinate_y = ballMovement(ball_coordinate_x, ball_coordinate_y, slope_8, intercept_8)
            elif ball_coordinate_y > 0:
                ball_coordinate_x, ball_coordinate_y = ballMovement(ball_coordinate_x, ball_coordinate_y, slope_6, intercept_6)

        if Array_index[0] == 6:
            if ball_coordinate_y > team_blue_2Y:
                ball_coordinate_x, ball_coordinate_y = ballMovement(ball_coordinate_x, ball_coordinate_y, slope_2, intercept_2)
            elif ball_coordinate_y > team_blue_3Y:
                ball_coordinate_x, ball_coordinate_y = ballMovement(ball_coordinate_x, ball_coordinate_y, slope_9, intercept_9)
            elif ball_coordinate_y > 0:
                ball_coordinate_x, ball_coordinate_y = ballMovement(ball_coordinate_x, ball_coordinate_y, slope_6, intercept_6)

        if Array_index[0] == 7:
            if ball_coordinate_y > team_blue_2Y:
                ball_coordinate_x, ball_coordinate_y = ballMovement(ball_coordinate_x, ball_coordinate_y, slope_2, intercept_2)
            elif ball_coordinate_y > team_blue_1Y:
                ball_coordinate_x, ball_coordinate_y = ballMovement(ball_coordinate_x, ball_coordinate_y, slope_7, intercept_7)
            elif ball_coordinate_y > 0:
                ball_coordinate_x, ball_coordinate_y = ballMovement(ball_coordinate_x, ball_coordinate_y, slope_4, intercept_4)

        if Array_index[0] == 8:
            if ball_coordinate_y > team_blue_3Y:
                ball_coordinate_x, ball_coordinate_y = ballMovement(ball_coordinate_x, ball_coordinate_y, slope_3, intercept_3)
            elif ball_coordinate_y > team_blue_2Y:
                ball_coordinate_x, ball_coordinate_y = ballMovement(ball_coordinate_x, ball_coordinate_y, slope_9, intercept_9)
            elif ball_coordinate_y > 0:
                ball_coordinate_x, ball_coordinate_y = ballMovement(ball_coordinate_x, ball_coordinate_y, slope_5, intercept_5)

        if Array_index[0] == 9:
            if ball_coordinate_y > team_blue_3Y:
                ball_coordinate_x, ball_coordinate_y = ballMovement(ball_coordinate_x, ball_coordinate_y, slope_3, intercept_3)
            elif ball_coordinate_y > team_blue_1Y:
                ball_coordinate_x, ball_coordinate_y = ballMovement(ball_coordinate_x, ball_coordinate_y, slope_8, intercept_8)
            elif ball_coordinate_y > 0:
                ball_coordinate_x, ball_coordinate_y = ballMovement(ball_coordinate_x, ball_coordinate_y, slope_4, intercept_4)

        if Array_index[0] == 10:
            if ball_coordinate_y > team_blue_1Y:
                ball_coordinate_x, ball_coordinate_y = ballMovement(ball_coordinate_x, ball_coordinate_y, slope_1, intercept_1)
            elif ball_coordinate_y > team_blue_2Y:
                ball_coordinate_x, ball_coordinate_y = ballMovement(ball_coordinate_x, ball_coordinate_y, slope_7, intercept_7)
            elif ball_coordinate_y > team_blue_3Y:
                ball_coordinate_x, ball_coordinate_y = ballMovement(ball_coordinate_x, ball_coordinate_y, slope_9, intercept_9)
            elif ball_coordinate_y > 0:
                ball_coordinate_x, ball_coordinate_y = ballMovement(ball_coordinate_x, ball_coordinate_y, slope_6, intercept_6)

        if Array_index[0] == 11:
            if ball_coordinate_y > team_blue_1Y:
                ball_coordinate_x, ball_coordinate_y = ballMovement(ball_coordinate_x, ball_coordinate_y, slope_1, intercept_1)
            elif ball_coordinate_y > team_blue_3Y:
                ball_coordinate_x, ball_coordinate_y = ballMovement(ball_coordinate_x, ball_coordinate_y, slope_8, intercept_8)
            elif ball_coordinate_y > team_blue_2Y:
                ball_coordinate_x, ball_coordinate_y = ballMovement(ball_coordinate_x, ball_coordinate_y, slope_9, intercept_9)
            elif ball_coordinate_y > 0:
                ball_coordinate_x, ball_coordinate_y = ballMovement(ball_coordinate_x, ball_coordinate_y, slope_5, intercept_5)

        if Array_index[0] == 12:
            if ball_coordinate_y > team_blue_2Y:
                ball_coordinate_x, ball_coordinate_y = ballMovement(ball_coordinate_x, ball_coordinate_y, slope_2, intercept_2)
            elif ball_coordinate_y > team_blue_3Y:
                ball_coordinate_x, ball_coordinate_y = ballMovement(ball_coordinate_x, ball_coordinate_y, slope_9, intercept_9)
            elif ball_coordinate_y > team_blue_1Y:
                ball_coordinate_x, ball_coordinate_y = ballMovement(ball_coordinate_x, ball_coordinate_y, slope_8, intercept_8)
            elif ball_coordinate_y > 0:
                ball_coordinate_x, ball_coordinate_y = ballMovement(ball_coordinate_x, ball_coordinate_y, slope_4, intercept_4)

        if Array_index[0] == 13:
            if ball_coordinate_y > team_blue_2Y:
                ball_coordinate_x, ball_coordinate_y = ballMovement(ball_coordinate_x, ball_coordinate_y, slope_2, intercept_2)
            elif ball_coordinate_y > team_blue_1Y:
                ball_coordinate_x, ball_coordinate_y = ballMovement(ball_coordinate_x, ball_coordinate_y, slope_7, intercept_7)
            elif ball_coordinate_y > team_blue_3Y:
                ball_coordinate_x, ball_coordinate_y = ballMovement(ball_coordinate_x, ball_coordinate_y, slope_8, intercept_8)
            elif ball_coordinate_y > 0:
                ball_coordinate_x, ball_coordinate_y = ballMovement(ball_coordinate_x, ball_coordinate_y, slope_6, intercept_6)

        if Array_index[0] == 14:
            if ball_coordinate_y > team_blue_3Y:
                ball_coordinate_x, ball_coordinate_y = ballMovement(ball_coordinate_x, ball_coordinate_y, slope_3, intercept_3)
            elif ball_coordinate_y > team_blue_2Y:
                ball_coordinate_x, ball_coordinate_y = ballMovement(ball_coordinate_x, ball_coordinate_y, slope_9, intercept_9)
            elif ball_coordinate_y > team_blue_1Y:
                ball_coordinate_x, ball_coordinate_y = ballMovement(ball_coordinate_x, ball_coordinate_y, slope_7, intercept_7)
            elif ball_coordinate_y > 0:
                ball_coordinate_x, ball_coordinate_y = ballMovement(ball_coordinate_x, ball_coordinate_y, slope_4, intercept_4)

        if Array_index[0] == 15:
            if ball_coordinate_y > team_blue_3Y:
                ball_coordinate_x, ball_coordinate_y = ballMovement(ball_coordinate_x, ball_coordinate_y, slope_3, intercept_3)
            elif ball_coordinate_y > team_blue_1Y:
                ball_coordinate_x, ball_coordinate_y = ballMovement(ball_coordinate_x, ball_coordinate_y, slope_8, intercept_8)
            elif ball_coordinate_y > team_blue_2Y:
                ball_coordinate_x, ball_coordinate_y = ballMovement(ball_coordinate_x, ball_coordinate_y, slope_7, intercept_7)
            elif ball_coordinate_y > 0:
                ball_coordinate_x, ball_coordinate_y = ballMovement(ball_coordinate_x, ball_coordinate_y, slope_5, intercept_5)

        if ball_coordinate_y<32:
            screen.blit(cost3, costRect3)


    pygame.display.update()
