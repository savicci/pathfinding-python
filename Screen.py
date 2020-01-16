#!usr/bin/python3
import pygame
from threading import Thread

import Grid
import ButtonBar
from astar import astar

modes = {
    'RUN': 'Run',
    'START': 'Start'
}

colors = {
    'WHITE': (255, 255, 255)
}

size = (20, 40)
boxSize = 30


class Screen:
    def __init__(self, width, height, fps):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.start = None
        self.end = None

        self.buttonBar = ButtonBar.ButtonBar(self.screen, width, height)
        self.grid = Grid.Grid(self.screen, 40, 80, size[0], size[1], boxSize)

        pygame.display.set_caption('A* pathfinding algorithm visualization')


    def begin(self):
        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    done = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.handleMouseClick()

            if self.buttonBar.mode == 'Run':
                thread = Thread(target = self.startVisualization, args=(self.grid.grid, self.start, self.end))
                thread.start()
                self.buttonBar.mode = 'Start'
            
            self.screen.fill(colors['WHITE'])
            self.grid.draw(self.start, self.end)
            self.buttonBar.draw()

            pygame.display.flip()
            self.clock.tick(self.fps)


    def startVisualization(self, grid, start, end):
        if start == None or end == None:
            return

        result = astar(grid, start, end)

        if result == None:
            return

        for i in result:
            self.grid.grid[i[0]][i[1]] = 3
    
        
    def handleMouseClick(self):
        pos = pygame.mouse.get_pos()

        # should update blocks
        if ( pos[0] >= 40 and pos[0] <= 1210 + boxSize ) and (pos[1] >= 80  and pos[1] <= 650 + boxSize):
            (self.start, self.end) = self.grid.updateBlock(pos, self.buttonBar.mode, self.start, self.end)

        #should change mode
        if (pos[0] >= 40 and pos[0] <= 440 + 80) and (pos[1] >= 10 and pos[1] <= 10 + 40):
            self.buttonBar.changeMode(pos)

            if self.buttonBar.mode == 'Clear':
                self.grid.clear()
                self.buttonBar.mode = 'Start'



if __name__ == "__main__":
    pygame.init()

    screen = Screen(1280, 720, 30)
    screen.begin()