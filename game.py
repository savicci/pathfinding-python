#!usr/bin/python3
import pygame
from astar import astar
from enum import Enum

# colors used to color the screen
START = (252, 3, 3)
END = (3, 3, 252)
BLOCK = (140, 140, 140)
SCREEN = (255, 255, 255)
RECTANGLE = (0, 0, 0)
TEXT = (0, 0, 0)
 


# initialize pygame modules
pygame.init()

# global variables
screen_width = 1280
screen_height = 720

table_start_x = 40
table_start_y = 80

rows = 20
columns = 40

box_size = 30

frames_per_second = 60


screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('A* pathfinding algorithm visualization')
clock = pygame.time.Clock()



def createTable():
    global size
    return [[0 for i in range(columns)] for i in range(rows)]


# draws a single point from table on screen
def drawRectangle(x, y, value):
    global box_size, screen
    
    if value == 0: type = RECTANGLE
    elif value == 1: type = BLOCK
    elif value == 2: type = START
    else: type = END

    pygame.draw.rect(screen, type, (x,y,box_size, box_size), 1)



# iterate over every element and draw it on screen
def drawTable(table):
    global table_start_x, table_start_y

    for iidx, row in enumerate(table):
        for jidx, column in enumerate(row):
            drawRectangle(table_start_x + jidx*box_size, table_start_y + iidx*box_size, column)

# draw start, end, and block buttons
def drawButtons():
    global screen
    
    font = pygame.font.SysFont('Arial', 25)
    pygame.draw.rect(screen, START, (40, 10, 80, 40), 1)
    screen.blit(font.render('Start', True, RECTANGLE, None), (30,20))
    pygame.display.update()





def handleMouseClick():
    pos = pygame.mouse.get_pos()
    
    # should update blocks
    if ( pos[0] >= 40 and pos[0] <= 1210 + box_size ) and (pos[1] >= 80  and pos[1] <= 650 + box_size):
        print('I will update blocks')





def setUpVisualization():
    global screen 

    done = False 

    table = createTable()

    while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    done = True
                if event.type == pygame.MOUSEBUTTONUP:
                    handleMouseClick()
                    
                    



        screen.fill(SCREEN)

        drawTable(table)
        drawButtons()

        pygame.display.flip()
        clock.tick(frames_per_second)



if __name__ == '__main__':
    setUpVisualization()