#!usr/bin/python3
import pygame
from astar import astar
from enum import Enum
from threading import Thread

# colors used to color the screen
START = (252, 3, 3)
END = (3, 3, 252)
BLOCK = (140, 140, 140)
SCREEN = (255, 255, 255)
RECTANGLE = (0, 0, 0)
TEXT = (0, 0, 0)
PATH = (97, 235, 52)
STEP = (66, 245, 191)
 

# initialize pygame modules
pygame.init()

# global variables
screen_width = 1280
screen_height = 720

start = None
end = None


startButton = None
endButton = None
blockButton = None
runButton = None

rows = 20
columns = 40

box_size = 30

frames_per_second = 60


screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('A* pathfinding algorithm visualization')
clock = pygame.time.Clock()

mode = 'Start'

def createTable():
    global size
    return [[0 for i in range(columns)] for i in range(rows)]

table = createTable()
table_start_x = 40
table_start_y = 80


# draws a single point from table on screen
def drawRectangle(x, y, value):
    global box_size, screen
    
    if value == 0: type = RECTANGLE
    elif value == 1: type = BLOCK
    else: pass

    if value == 0:
        pygame.draw.rect(screen, type, (x,y,box_size, box_size), 1)
    else:
        pygame.draw.rect(screen, type, (x,y,box_size, box_size))


# iterate over every element and draw it on screen
def drawTable():
    global table, table_start_x, table_start_y

    for iidx, row in enumerate(table):
        for jidx, column in enumerate(row):
            if (iidx, jidx) == start:
                pygame.draw.rect(screen, START, (table_start_x + jidx*box_size, table_start_y + iidx*box_size , box_size, box_size))
            elif (iidx,jidx) == end:
                pygame.draw.rect(screen, END, (table_start_x + jidx*box_size, table_start_y + iidx*box_size, box_size, box_size))
            elif table[iidx][jidx] == 7:
                pygame.draw.rect(screen, STEP, (table_start_x + jidx*box_size, table_start_y + iidx*box_size, box_size, box_size))
            elif table[iidx][jidx] == 5:
                pygame.draw.rect(screen, PATH, (table_start_x + jidx*box_size, table_start_y + iidx*box_size, box_size, box_size))
            elif table[iidx][jidx] != 5:
                drawRectangle(table_start_x + jidx*box_size, table_start_y + iidx*box_size, column)


# draw start, end, and block buttons
def drawButtons():
    global screen, mode, startButton, endButton, blockButton, runButton
    
    font = pygame.font.SysFont('Arial', 25)
    startButton = pygame.draw.rect(screen, START, (40, 10, 80, 40))
    screen.blit(font.render('Start', True, RECTANGLE, None), (60,20))

    endButton = pygame.draw.rect(screen, END, (140, 10, 80, 40))
    screen.blit(font.render('End', True, RECTANGLE, None), (165,20))

    blockButton = pygame.draw.rect(screen, BLOCK, (240, 10, 80, 40))
    screen.blit(font.render('Block', True, RECTANGLE, None), (260, 20))

    runButton = pygame.draw.rect(screen, RECTANGLE, (340, 10, 80, 40))
    screen.blit(font.render('Run', True, SCREEN, None), (365, 20))

    screen.blit(font.render('Mode chosen: {}'.format(mode), True, RECTANGLE, None), (465, 20))

    pygame.display.update()


def handleMouseClick():
    pos = pygame.mouse.get_pos()
    
    # should update blocks
    if ( pos[0] >= 40 and pos[0] <= 1210 + box_size ) and (pos[1] >= 80  and pos[1] <= 650 + box_size):
        updateBlock()

    #should change mode
    if (pos[0] >= 40 and pos[0] <= 340 + 80) and (pos[1] >= 10 and pos[1] <= 10 + 40):
        changeMode()


def updateBlock():
    global screen, table, table_start_x, table_start_y, box_size, start, end

    pos = pygame.mouse.get_pos()

    row = 0
    col = 0

    while True:
        if (pos[0] >= table_start_x + col*box_size + box_size):
            col +=1
        else: break

    while True:
        if(pos[1] >= table_start_y + row*box_size + box_size):
            row +=1
        else: break
    
    print(row, col)

    if mode == 'Start':
        start = (row, col)
    elif mode == 'End':
        end = (row, col)
    elif mode == 'Block':
        if table[row][col] == 1:
            table[row][col] = 0
        else: 
            table[row][col] = 1
    else:
        pass

    



# if hit any of the buttons change mode
def changeMode():
    global mode,startButton, endButton, blockButton, runButton

    pos = pygame.mouse.get_pos()

    if startButton.collidepoint(pos[0], pos[1]):
        mode = 'Start'
    elif endButton.collidepoint(pos[0], pos[1]):
        mode = 'End'
    elif blockButton.collidepoint(pos[0], pos[1]):
        mode = 'Block'
    elif runButton.collidepoint(pos[0], pos[1]):
        mode = 'Run'


def runVisualization():
    global table, start, end
    # print(table)
    # print(start)
    # print(end)
    result = astar(table, start, end)
    
    for i in result:
        table[i[0]][i[1]] = 5



def setUpVisualization():
    global screen, mode, table, start, end 

    done = False
    steps = []
    path = []

    while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    done = True
                if event.type == pygame.MOUSEBUTTONUP:
                    handleMouseClick()
                    

        if mode == 'Run':
            thread = Thread(target = runVisualization, args=())
            thread.start()
            print('hello in main')
            mode = 'Block'


        screen.fill(SCREEN)

        drawTable()
        drawButtons()

        pygame.display.flip()
        clock.tick(frames_per_second)



if __name__ == '__main__':
    setUpVisualization()